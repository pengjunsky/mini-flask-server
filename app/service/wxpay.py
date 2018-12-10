import time
from hashlib import md5
import uuid
from flask import current_app
import xml.etree.ElementTree as ET
from app.libs.error_code import WeChatException
from app.libs.httper import Http


class Base:
    @staticmethod
    def create_sign(pay_data):
        # 生成签名
        merchant_key = current_app.config['MERCHANT_KEY']
        stringA = '&'.join(["{0}={1}".format(k, pay_data.get(k)) for k in sorted(pay_data)])
        stringSignTemp = '{0}&key={1}'.format(stringA, merchant_key)
        sign = md5(stringSignTemp.encode('utf-8')).hexdigest()
        return sign.upper()

    @staticmethod
    def dict_to_xml(pay_data):
        xml = ["<xml>"]
        for k, v in pay_data.items():
            xml.append("<{0}>{1}</{0}>".format(k, v))
        xml.append("</xml>")
        return "".join(xml)

    @staticmethod
    def xml_to_dict(xml_data):
        xml_dict = {}
        root = ET.fromstring(xml_data)
        for child in root:
            xml_dict[child.tag] = child.text
        return xml_dict

    @staticmethod
    def get_nonce_str():
        # 获取随机字符串
        return str(uuid.uuid4()).replace('-', '')

    @staticmethod
    def process_login_error(wx_result):
        raise WeChatException(
            msg=wx_result['return_msg']
        )


class UnifiedOrder(Base):
    # 小程序统一下单功能
    def __init__(self, oid, openid, pay_price):
        self.unified_order_url = current_app.config['UNIFIED_ORDER']
        self.pay_data = {
            'appid': current_app.config['APP_ID'],
            'mch_id': current_app.config['MCH_ID'],
            'nonce_str': self.get_nonce_str(),
            'body': '测试',  # 商品描述
            'out_trade_no': oid,  # 商户订单号
            'total_fee': int(pay_price * 100),
            'spbill_create_ip': current_app.config['LOCAL_IP'],
            'notify_url': current_app.config['NOTIFY_URL'],
            'trade_type': current_app.config['TRADE_TYPE'],
            'openid': openid
        }

    def get_pay_info(self):
        # 获取支付信息
        sign = self.create_sign(self.pay_data)
        self.pay_data['sign'] = sign
        xml_data = self.dict_to_xml(self.pay_data)
        headers = {'Content-Type': 'application/xml'}
        response = Http.post(self.unified_order_url, xml_data, headers, return_json=False)
        if response:
            wx_result = self.xml_to_dict(response)
            if wx_result.get('return_code') == 'FAIL':
                self.process_login_error(wx_result)
            else:
                prepay_id = wx_result.get('prepay_id')
                pay_sign_data = {
                    'appId': self.pay_data.get('appid'),
                    'timeStamp': str(int(time.time())),
                    'nonceStr': self.pay_data.get('nonce_str'),
                    'package': 'prepay_id={0}'.format(prepay_id),
                    'signType': 'MD5'
                }
                pay_sign = self.create_sign(pay_sign_data)
                pay_sign_data.pop('appId')
                pay_sign_data['paySign'] = pay_sign
                return pay_sign_data
        else:
            raise Exception()


class OrderQuery(Base):
    # 订单查询功能类
    def __init__(self, oid):
        self.order_query_url = current_app.config['ORDER_QUERY']
        self.pay_data = {
            'appid': current_app.config['APP_ID'],
            'mch_id': current_app.config['MCH_ID'],
            'out_trade_no': oid,  # 商户订单号
            'nonce_str': self.get_nonce_str(),
        }

    def get_pay_info(self):
        sign = self.create_sign(self.pay_data)
        self.pay_data['sign'] = sign
        xml_data = self.dict_to_xml(self.pay_data)
        headers = {'Content-Type': 'application/xml'}
        response = Http.post(self.order_query_url, xml_data, headers, return_json=False)
        if response:
            wx_result = self.xml_to_dict(response)
            if wx_result.get('return_code') == 'FAIL':
                self.process_login_error(wx_result)
            else:
                return wx_result
        else:
            raise Exception()
