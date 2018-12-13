/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : mall

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-12-13 16:30:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `banner`
-- ----------------------------
DROP TABLE IF EXISTS `banner`;
CREATE TABLE `banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL COMMENT 'Banner名称，通常作为标识',
  `description` varchar(255) DEFAULT NULL COMMENT 'Banner描述',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='banner管理表';

-- ----------------------------
-- Records of banner
-- ----------------------------
INSERT INTO `banner` VALUES ('1', '首页置顶', '首页轮播图', null, '1528938338');

-- ----------------------------
-- Table structure for `banner_item`
-- ----------------------------
DROP TABLE IF EXISTS `banner_item`;
CREATE TABLE `banner_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_id` int(11) NOT NULL COMMENT '外键，关联image表',
  `key_word` varchar(100) NOT NULL COMMENT '执行关键字，根据不同的type含义不同',
  `type` tinyint(4) NOT NULL DEFAULT '1' COMMENT '跳转类型，可能导向商品，可能导向专题，可能导向其他。0，无导向；1：导向商品;2:导向专题',
  `banner_id` int(11) NOT NULL COMMENT '外键，关联banner表',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COMMENT='banner子项表';

-- ----------------------------
-- Records of banner_item
-- ----------------------------
INSERT INTO `banner_item` VALUES ('1', '65', '6', '1', '1', null, '1528938338');
INSERT INTO `banner_item` VALUES ('2', '2', '25', '1', '1', null, '1528938338');
INSERT INTO `banner_item` VALUES ('3', '3', '11', '1', '1', null, '1528938338');
INSERT INTO `banner_item` VALUES ('5', '1', '10', '1', '1', null, '1528938338');

-- ----------------------------
-- Table structure for `cart`
-- ----------------------------
DROP TABLE IF EXISTS `cart`;
CREATE TABLE `cart` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL COMMENT '商品ID',
  `property_id` int(11) DEFAULT NULL COMMENT '属性ID',
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `qty` int(11) DEFAULT '1' COMMENT '数量',
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`property_id`) REFERENCES `product_property` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of cart
-- ----------------------------

-- ----------------------------
-- Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL COMMENT '分类名称',
  `topic_img_id` int(11) DEFAULT NULL COMMENT '外键，关联image表',
  `description` varchar(100) DEFAULT NULL COMMENT '描述',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COMMENT='商品类目';

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('2', '果味', '6', null, null, null);
INSERT INTO `category` VALUES ('3', '蔬菜', '5', null, null, null);
INSERT INTO `category` VALUES ('4', '炒货', '7', null, null, null);
INSERT INTO `category` VALUES ('5', '点心', '4', null, null, null);
INSERT INTO `category` VALUES ('6', '粗茶', '8', null, null, null);
INSERT INTO `category` VALUES ('7', '淡饭', '9', null, null, null);

-- ----------------------------
-- Table structure for `comment`
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `product_id` int(11) NOT NULL COMMENT '商品ID',
  `content` varchar(100) DEFAULT NULL COMMENT '评论内容',
  `type` int(11) DEFAULT NULL COMMENT '评价分类1好评2中评3差评',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES (null, null, '1', '1', '11', '你个哈皮', '1');

-- ----------------------------
-- Table structure for `coupon`
-- ----------------------------
DROP TABLE IF EXISTS `coupon`;
CREATE TABLE `coupon` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float(6,2) NOT NULL,
  `title` varchar(24) NOT NULL,
  `label` varchar(50) NOT NULL,
  `qty` int(11) DEFAULT NULL,
  `n_price` int(11) DEFAULT NULL,
  `n_product` int(11) DEFAULT NULL,
  `n_category` int(11) DEFAULT NULL,
  `dead_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of coupon
-- ----------------------------
INSERT INTO `coupon` VALUES (null, null, '1', '1.00', '全店满减', '优惠卷', '11', '11', null, null, '1545515390');
INSERT INTO `coupon` VALUES (null, null, '2', '1.00', '生鲜优惠', '生鲜优惠', '11', null, '11', null, '1545515390');

-- ----------------------------
-- Table structure for `image`
-- ----------------------------
DROP TABLE IF EXISTS `image`;
CREATE TABLE `image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL COMMENT '图片路径',
  `from` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1 来自本地，2 来自公网',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COMMENT='图片总表';

-- ----------------------------
-- Records of image
-- ----------------------------
INSERT INTO `image` VALUES ('1', '/banner-1a.png', '1', null, null);
INSERT INTO `image` VALUES ('2', '/banner-2a.png', '1', null, null);
INSERT INTO `image` VALUES ('3', '/banner-3a.png', '1', null, null);
INSERT INTO `image` VALUES ('4', '/category-cake.png', '1', null, null);
INSERT INTO `image` VALUES ('5', '/category-vg.png', '1', null, null);
INSERT INTO `image` VALUES ('6', '/category-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('7', '/category-fry-a.png', '1', null, null);
INSERT INTO `image` VALUES ('8', '/category-tea.png', '1', null, null);
INSERT INTO `image` VALUES ('9', '/category-rice.png', '1', null, null);
INSERT INTO `image` VALUES ('10', '/product-dryfruit@1.png', '1', null, null);
INSERT INTO `image` VALUES ('13', '/product-vg@1.png', '1', null, null);
INSERT INTO `image` VALUES ('14', '/product-rice@6.png', '1', null, null);
INSERT INTO `image` VALUES ('16', '/1@theme.png', '1', null, null);
INSERT INTO `image` VALUES ('17', '/2@theme.png', '1', null, null);
INSERT INTO `image` VALUES ('18', '/3@theme.png', '1', null, null);
INSERT INTO `image` VALUES ('19', '/detail-1@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('20', '/detail-2@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('21', '/detail-3@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('22', '/detail-4@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('23', '/detail-5@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('24', '/detail-6@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('25', '/detail-7@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('26', '/detail-8@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('27', '/detail-9@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('28', '/detail-11@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('29', '/detail-10@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('31', '/product-rice@1.png', '1', null, null);
INSERT INTO `image` VALUES ('32', '/product-tea@1.png', '1', null, null);
INSERT INTO `image` VALUES ('33', '/product-dryfruit@2.png', '1', null, null);
INSERT INTO `image` VALUES ('36', '/product-dryfruit@3.png', '1', null, null);
INSERT INTO `image` VALUES ('37', '/product-dryfruit@4.png', '1', null, null);
INSERT INTO `image` VALUES ('38', '/product-dryfruit@5.png', '1', null, null);
INSERT INTO `image` VALUES ('39', '/product-dryfruit-a@6.png', '1', null, null);
INSERT INTO `image` VALUES ('40', '/product-dryfruit@7.png', '1', null, null);
INSERT INTO `image` VALUES ('41', '/product-rice@2.png', '1', null, null);
INSERT INTO `image` VALUES ('42', '/product-rice@3.png', '1', null, null);
INSERT INTO `image` VALUES ('43', '/product-rice@4.png', '1', null, null);
INSERT INTO `image` VALUES ('44', '/product-fry@1.png', '1', null, null);
INSERT INTO `image` VALUES ('45', '/product-fry@2.png', '1', null, null);
INSERT INTO `image` VALUES ('46', '/product-fry@3.png', '1', null, null);
INSERT INTO `image` VALUES ('47', '/product-tea@2.png', '1', null, null);
INSERT INTO `image` VALUES ('48', '/product-tea@3.png', '1', null, null);
INSERT INTO `image` VALUES ('49', '/1@theme-head.png', '1', null, null);
INSERT INTO `image` VALUES ('50', '/2@theme-head.png', '1', null, null);
INSERT INTO `image` VALUES ('51', '/3@theme-head.png', '1', null, null);
INSERT INTO `image` VALUES ('52', '/product-cake@1.png', '1', null, null);
INSERT INTO `image` VALUES ('53', '/product-cake@2.png', '1', null, null);
INSERT INTO `image` VALUES ('54', '/product-cake-a@3.png', '1', null, null);
INSERT INTO `image` VALUES ('55', '/product-cake-a@4.png', '1', null, null);
INSERT INTO `image` VALUES ('56', '/product-dryfruit@8.png', '1', null, null);
INSERT INTO `image` VALUES ('57', '/product-fry@4.png', '1', null, null);
INSERT INTO `image` VALUES ('58', '/product-fry@5.png', '1', null, null);
INSERT INTO `image` VALUES ('59', '/product-rice@5.png', '1', null, null);
INSERT INTO `image` VALUES ('60', '/product-rice@7.png', '1', null, null);
INSERT INTO `image` VALUES ('62', '/detail-12@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('63', '/detail-13@1-dryfruit.png', '1', null, null);
INSERT INTO `image` VALUES ('65', '/banner-4a.png', '1', null, null);
INSERT INTO `image` VALUES ('66', '/product-vg@4.png', '1', null, null);
INSERT INTO `image` VALUES ('67', '/product-vg@5.png', '1', null, null);
INSERT INTO `image` VALUES ('68', '/product-vg@2.png', '1', null, null);
INSERT INTO `image` VALUES ('69', '/product-vg@3.png', '1', null, null);

-- ----------------------------
-- Table structure for `order`
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_no` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `total_price` float(6,2) NOT NULL,
  `pay_price` float(6,2) NOT NULL,
  `snap_address` varchar(500) NOT NULL,
  `coupon_price` float(6,2) DEFAULT NULL,
  `postage` int(11) DEFAULT NULL,
  `remark` varchar(100) DEFAULT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_no` (`order_no`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES ('1543995170', null, '18', 'A0XC515951443995214', '7', '7.07', '7.07', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1543995551', null, '19', 'A0XC551056243995645', '7', '1.00', '9.00', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '8', null, null, '1');
INSERT INTO `order` VALUES ('1543995578', null, '20', 'A0XC504134643995694', '7', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544060799', null, '21', 'A0XC614363444060839', '7', '1.00', '9.00', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '8', null, null, '1');
INSERT INTO `order` VALUES ('1544237341', null, '22', 'A0XC878803644237227', '7', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544237390', null, '23', 'A0XC873445244237137', '7', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544253753', null, '24', 'A0XC844143544253505', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544255649', null, '25', 'A0XC890944044255506', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544255718', null, '26', 'A0XC848239044255952', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, '4200000234201812088619363173', '2');
INSERT INTO `order` VALUES ('1544412145', null, '28', 'A0XC1031226244412426', '1', '0.03', '0.03', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544412902', null, '29', 'A0XC1045825244412863', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544514390', null, '30', 'A0XC1199061144514506', '1', '0.10', '8.10', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '8', null, null, '1');
INSERT INTO `order` VALUES ('1544514520', null, '31', 'A0XC1104289444514653', '1', '22.00', '19.00', '张三 020-81167888 广东省广州市海珠区新港中路397号', '11.00', '8', null, null, '1');
INSERT INTO `order` VALUES ('1544578181', null, '32', 'A0XC1251484244578384', '1', '22.00', '30.00', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '8', null, null, '1');
INSERT INTO `order` VALUES ('1544598791', null, '33', 'A0XC1265821944598217', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544682886', null, '34', 'A0XC1340023244682271', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, '4200000233201812130405713980', '2');
INSERT INTO `order` VALUES ('1544682936', null, '35', 'A0XC1376010044682110', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544684263', null, '36', 'A0XC1312917944684601', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, '4200000231201812132971642022', '2');
INSERT INTO `order` VALUES ('1544684497', null, '37', 'A0XC1346994344684970', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544684552', null, '38', 'A0XC1395552444684992', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');
INSERT INTO `order` VALUES ('1544684698', null, '39', 'A0XC1367765944684429', '1', '0.01', '0.01', '张三 020-81167888 广东省广州市海珠区新港中路397号', '0.00', '0', null, null, '1');

-- ----------------------------
-- Table structure for `order_snap`
-- ----------------------------
DROP TABLE IF EXISTS `order_snap`;
CREATE TABLE `order_snap` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_no` varchar(20) NOT NULL,
  `snap_name` varchar(80) NOT NULL,
  `snap_img_id` int(11) NOT NULL,
  `price` float(6,2) NOT NULL,
  `property_name` varchar(30) DEFAULT NULL,
  `count` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `property_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `snap_img_id` (`snap_img_id`),
  CONSTRAINT `order_snap_ibfk_1` FOREIGN KEY (`snap_img_id`) REFERENCES `image` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of order_snap
-- ----------------------------
INSERT INTO `order_snap` VALUES ('1543995170', null, '29', 'A0XC515951443995214', '贵妃笑 100克贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑', '39', '1.00', '1000g', '7', '11', '7');
INSERT INTO `order_snap` VALUES ('1543995170', null, '30', 'A0XC515951443995214', '锈色瓜子 100克', '57', '0.01', null, '3', '27', null);
INSERT INTO `order_snap` VALUES ('1543995170', null, '31', 'A0XC515951443995214', '红衣青瓜 混搭160克', '56', '0.01', null, '4', '26', null);
INSERT INTO `order_snap` VALUES ('1543995551', null, '32', 'A0XC551056243995645', '贵妃笑 100克贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑', '39', '1.00', '1000g', '1', '11', '7');
INSERT INTO `order_snap` VALUES ('1543995578', null, '33', 'A0XC504134643995694', '冰心鸡蛋 2个', '59', '0.01', null, '1', '29', null);
INSERT INTO `order_snap` VALUES ('1544060799', null, '34', 'A0XC614363444060839', '贵妃笑 100克贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑', '39', '1.00', '1000g', '1', '11', '7');
INSERT INTO `order_snap` VALUES ('1544237341', null, '35', 'A0XC878803644237227', '万紫千凤梨 300克', '38', '0.01', null, '1', '10', null);
INSERT INTO `order_snap` VALUES ('1544237390', null, '36', 'A0XC873445244237137', '土豆 半斤', '66', '0.01', null, '1', '32', null);
INSERT INTO `order_snap` VALUES ('1544253753', null, '37', 'A0XC844143544253505', '梅兰清花糕 1个', '54', '0.01', null, '1', '22', null);
INSERT INTO `order_snap` VALUES ('1544255649', null, '38', 'A0XC890944044255506', '春泥花生 200克', '58', '0.01', null, '1', '28', null);
INSERT INTO `order_snap` VALUES ('1544255718', null, '39', 'A0XC848239044255952', '土豆 半斤', '66', '0.01', null, '1', '32', null);
INSERT INTO `order_snap` VALUES ('1544408412', null, '40', 'A0XC1040292244408974', '土豆 半斤', '66', '0.01', null, '1', '32', null);
INSERT INTO `order_snap` VALUES ('1544412145', null, '41', 'A0XC1031226244412426', '红衣青瓜 混搭160克', '56', '0.01', null, '3', '26', null);
INSERT INTO `order_snap` VALUES ('1544412902', null, '42', 'A0XC1045825244412863', '小明的妙脆角 120克', '52', '0.01', null, '1', '25', null);
INSERT INTO `order_snap` VALUES ('1544514390', null, '43', 'A0XC1199061144514506', '贵妃笑 100克贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑', '39', '0.10', '500g', '1', '11', '1');
INSERT INTO `order_snap` VALUES ('1544514520', null, '44', 'A0XC1104289444514653', '贵妃笑 100克贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑', '39', '11.00', '1000g', '2', '11', '8');
INSERT INTO `order_snap` VALUES ('1544578181', null, '45', 'A0XC1251484244578384', '贵妃笑 100克贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑', '39', '11.00', '1000g', '2', '11', '8');
INSERT INTO `order_snap` VALUES ('1544598791', null, '46', 'A0XC1265821944598217', '深涧木耳 78克', '60', '0.01', null, '1', '31', null);
INSERT INTO `order_snap` VALUES ('1544682886', null, '47', 'A0XC1340023244682271', '碧螺春 12克*3袋', '47', '0.01', null, '1', '20', null);
INSERT INTO `order_snap` VALUES ('1544682936', null, '48', 'A0XC1376010044682110', '西湖龙井 8克*3袋', '48', '0.01', null, '1', '21', null);
INSERT INTO `order_snap` VALUES ('1544684263', null, '49', 'A0XC1312917944684601', '冰心鸡蛋 2个', '59', '0.01', null, '1', '29', null);
INSERT INTO `order_snap` VALUES ('1544684497', null, '50', 'A0XC1346994344684970', '深涧木耳 78克', '60', '0.01', null, '1', '31', null);
INSERT INTO `order_snap` VALUES ('1544684552', null, '51', 'A0XC1395552444684992', '深涧木耳 78克', '60', '0.01', null, '1', '31', null);
INSERT INTO `order_snap` VALUES ('1544684698', null, '52', 'A0XC1367765944684429', '锈色瓜子 100克', '57', '0.01', null, '1', '27', null);

-- ----------------------------
-- Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL COMMENT '商品名称',
  `originalPrice` decimal(6,2) DEFAULT NULL COMMENT '原始价格',
  `price` decimal(6,2) NOT NULL COMMENT '价格,单位：分',
  `sale` int(11) NOT NULL DEFAULT '0' COMMENT '销量',
  `content` varchar(5000) DEFAULT NULL COMMENT '详情',
  `stock` int(11) NOT NULL DEFAULT '0' COMMENT '库存量',
  `category_id` int(11) DEFAULT NULL,
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL,
  `summary` varchar(50) DEFAULT NULL COMMENT '摘要',
  `main_img_id` int(11) DEFAULT NULL COMMENT '图片外键',
  `postage` int(11) NOT NULL DEFAULT '0' COMMENT '邮费',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES ('1', '芹菜 半斤', null, '0.01', '0', '<div style=\"font-family: &quot;Microsoft YaHei&quot;; font-size: 14px; text-indent: 28px; white-space: normal;\">\r\n    <span style=\"font-size: 28px; font-weight: bold; color: rgb(102, 102, 102);\">UMeditor</span>,简称UM,是为满足广大门户网站对于简单发帖框，或者回复框需求所定制的在线富文本编辑器。 UM的主要特点就是容量和加载速度上的改变，主文件的代码量为139k，而且放弃了使用传统的iframe模式，采用了div的加载方式， 以达到更快的加载速度和零加载失败率。现在UM的第一个使用者是百度贴吧，贴吧每天几亿的pv是对UM各种指标的最好测试平台。 当然随着代码的减少，UM的功能对于UE来说还是有所减少，但我们经过调研和大家对于UM提出的各种意见，提供了现在UM的功能版本， 虽然有删减，但也有增加，比如拖拽图片上传，chrome的图片拖动改变大小等。让UM能在功能和体积上达到一个平衡。UM还会提供 CDN方式，减少大家部署的成本。我们的目标不仅是要提高在线编辑的编辑体验，也希望能改变前端技术中关于富文本技术的门槛，让大家不再觉得这块是个大坑。\r\n</div>\r\n<div style=\"font-family: &quot;Microsoft YaHei&quot;; font-size: 14px; text-indent: 2em; white-space: normal; margin: 20px; line-height: 22px; color: red;\">\r\n    紧急修复了 UMEditor 的 xss 漏洞，请下载最新版更新。2016-12-22&nbsp;<br/>xss过滤白名单中去掉 iframe，防止xss漏洞，例如源码模式下直接复制：&lt;iframe src=&quot;javascript:alert(1);&quot;&gt;&lt;/iframe&gt;\r\n</div>', '998', '3', '1528938338', null, null, '13', '0');
INSERT INTO `product` VALUES ('2', '梨花带雨 3个', null, '0.01', '0', null, '984', '2', '1528938339', null, null, '10', '0');
INSERT INTO `product` VALUES ('3', '素米 327克', null, '0.01', '0', null, '996', '7', '1528938340', null, null, '31', '0');
INSERT INTO `product` VALUES ('4', '红袖枸杞 6克*3袋', null, '0.01', '0', null, '998', '6', '1528938341', null, null, '32', '0');
INSERT INTO `product` VALUES ('5', '春生龙眼 500克', null, '0.01', '0', null, '995', '2', '1528938342', null, null, '33', '0');
INSERT INTO `product` VALUES ('6', '小红的猪耳朵 120克', null, '0.01', '0', null, '997', '5', '1528938343', null, null, '53', '0');
INSERT INTO `product` VALUES ('7', '泥蒿 半斤', null, '0.01', '0', null, '998', '3', '1528938344', null, null, '68', '0');
INSERT INTO `product` VALUES ('8', '夏日芒果 3个', null, '0.01', '0', null, '995', '2', '1528938345', null, null, '36', '0');
INSERT INTO `product` VALUES ('9', '冬木红枣 500克', null, '0.01', '0', null, '996', '2', '1528938346', null, null, '37', '0');
INSERT INTO `product` VALUES ('10', '万紫千凤梨 300克', null, '0.01', '0', null, '995', '2', '1528938347', null, null, '38', '0');
INSERT INTO `product` VALUES ('11', '贵妃笑 100克贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑贵妃笑', '100.00', '0.01', '0', '', '111', '2', '1528938369', null, '新鲜爽口，风味极佳。', '39', '8');
INSERT INTO `product` VALUES ('12', '珍奇异果 3个', null, '0.01', '0', null, '999', '2', '1528938349', null, null, '40', '0');
INSERT INTO `product` VALUES ('13', '绿豆 125克', null, '0.01', '0', null, '999', '7', '1528938350', null, null, '41', '0');
INSERT INTO `product` VALUES ('14', '芝麻 50克', null, '0.01', '0', null, '999', '7', '1528938351', null, null, '42', '0');
INSERT INTO `product` VALUES ('15', '猴头菇 370克', null, '0.01', '0', null, '999', '7', '1528938352', null, null, '43', '0');
INSERT INTO `product` VALUES ('16', '西红柿 1斤', null, '0.01', '0', null, '999', '3', '1528938353', null, null, '69', '0');
INSERT INTO `product` VALUES ('17', '油炸花生 300克', null, '0.01', '0', null, '999', '4', '1528938354', null, null, '44', '0');
INSERT INTO `product` VALUES ('18', '春泥西瓜子 128克', null, '0.01', '0', null, '997', '4', '1528938355', null, null, '45', '0');
INSERT INTO `product` VALUES ('19', '碧水葵花籽 128克', null, '0.01', '0', null, '999', '4', '1528938356', null, null, '46', '0');
INSERT INTO `product` VALUES ('20', '碧螺春 12克*3袋', null, '0.01', '0', null, '998', '6', '1528938357', null, null, '47', '0');
INSERT INTO `product` VALUES ('21', '西湖龙井 8克*3袋', null, '0.01', '0', null, '997', '6', '1528938358', null, null, '48', '0');
INSERT INTO `product` VALUES ('22', '梅兰清花糕 1个', null, '0.01', '0', null, '996', '5', '1528938359', null, null, '54', '0');
INSERT INTO `product` VALUES ('23', '清凉薄荷糕 1个', null, '0.01', '0', null, '998', '5', '1528938360', null, null, '55', '0');
INSERT INTO `product` VALUES ('25', '小明的妙脆角 120克', null, '0.01', '0', null, '998', '5', '1528938361', null, null, '52', '0');
INSERT INTO `product` VALUES ('26', '红衣青瓜 混搭160克', null, '0.01', '0', null, '992', '2', '1528938362', null, null, '56', '0');
INSERT INTO `product` VALUES ('27', '锈色瓜子 100克', null, '0.01', '0', null, '994', '4', '1528938363', null, null, '57', '0');
INSERT INTO `product` VALUES ('28', '春泥花生 200克', null, '0.01', '0', null, '998', '4', '1528938364', null, null, '58', '0');
INSERT INTO `product` VALUES ('29', '冰心鸡蛋 2个', null, '0.01', '0', null, '985', '7', '1528938365', null, null, '59', '0');
INSERT INTO `product` VALUES ('30', '八宝莲子 200克', null, '0.01', '0', null, '999', '7', '1528938366', null, null, '14', '0');
INSERT INTO `product` VALUES ('31', '深涧木耳 78克', null, '0.01', '0', null, '988', '7', '1528938367', null, null, '60', '0');
INSERT INTO `product` VALUES ('32', '土豆 半斤', null, '0.01', '0', null, '990', '3', '1528938368', null, null, '66', '0');
INSERT INTO `product` VALUES ('33', '青椒 半斤', null, '0.01', '0', null, '0', '3', '1528938369', null, null, '67', '0');

-- ----------------------------
-- Table structure for `product_image`
-- ----------------------------
DROP TABLE IF EXISTS `product_image`;
CREATE TABLE `product_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_id` int(11) NOT NULL COMMENT '外键，关联图片表',
  `order` int(11) NOT NULL DEFAULT '0' COMMENT '图片排序序号',
  `product_id` int(11) NOT NULL COMMENT '商品id，外键',
  `type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '图片类型 0，轮播展示图；1：详情图',
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product_image
-- ----------------------------
INSERT INTO `product_image` VALUES ('4', '19', '1', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('5', '20', '2', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('6', '21', '3', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('7', '22', '4', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('8', '23', '5', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('9', '24', '6', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('10', '25', '7', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('11', '26', '8', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('12', '27', '9', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('13', '28', '11', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('14', '29', '10', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('18', '62', '12', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('19', '63', '13', '11', '1', null, null);
INSERT INTO `product_image` VALUES ('20', '39', '1', '11', '0', null, null);

-- ----------------------------
-- Table structure for `product_property`
-- ----------------------------
DROP TABLE IF EXISTS `product_property`;
CREATE TABLE `product_property` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL COMMENT '属性名',
  `price` float(6,2) NOT NULL COMMENT '价格',
  `stock` int(11) NOT NULL DEFAULT '0' COMMENT '库存',
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `product_property_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product_property
-- ----------------------------
INSERT INTO `product_property` VALUES (null, null, '1', '500g', '0.10', '108', '11');
INSERT INTO `product_property` VALUES (null, null, '2', '1000g', '0.10', '105', '11');
INSERT INTO `product_property` VALUES (null, null, '4', '1000g', '1.00', '0', '11');
INSERT INTO `product_property` VALUES (null, null, '5', '1000g', '1.00', '0', '11');
INSERT INTO `product_property` VALUES (null, null, '6', '1000g', '1.00', '1', '11');
INSERT INTO `product_property` VALUES (null, null, '7', '1000g', '1.00', '94', '11');
INSERT INTO `product_property` VALUES (null, null, '8', '1000g', '11.00', '103', '11');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` varchar(50) DEFAULT NULL,
  `email` varchar(24) DEFAULT NULL,
  `nickname` varchar(24) DEFAULT NULL,
  `userPic` varchar(255) DEFAULT NULL,
  `auth` smallint(6) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `openid` (`openid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1539848235', '1540623233', '1', 'oapee4lTOfFg1hpx0lQ5x_HcURUM', null, '小毛', 'http://bmob-cdn-14612.b0.upaiyun.com/2017/12/19/cbe1427840f5c6b4801abcdd8b6a4e18.jpg', '1', null);
INSERT INTO `user` VALUES ('1539848235', null, '2', null, 'wwe1221@qq.com', 'nihaoe1212', null, '1', 'pbkdf2:sha256:50000$r070DVfB$bbd0d1995a7381c7d5c33cbe8aaa683653b44b3464cea77f4330138095530fce');
INSERT INTO `user` VALUES ('1540349983', null, '4', null, 'wwe12221@qq.com', 'nihaoe12212', null, '1', 'pbkdf2:sha256:50000$8FLGWA6K$f71dc8cae1ad00cc9ba7bca571400ab40835be02837cf3eb5db9bc9d4f87550b');
INSERT INTO `user` VALUES ('1540363560', null, '5', null, 'wwe122221@qq.com', 'nihaoe12212', null, '1', 'pbkdf2:sha256:50000$FjAW1u03$cf508e1ff3b562aec3c2eeea6a0bdde4eb678ddd79dba7ae26fbaab49bfd447f');
INSERT INTO `user` VALUES ('1540622646', null, '6', null, 'wwe1222221@qq.com', 'nihaoe122122', null, '1', 'pbkdf2:sha256:50000$8ibOAwHs$c573ce052f20036efe1af7afb61dd99a03fe45310505afe17b87bc10682af151');
INSERT INTO `user` VALUES ('1542938193', null, '7', 'oKmzy0FiI1q6tGaZEKs6cyrBzYfo', null, null, null, '1', null);

-- ----------------------------
-- Table structure for `user_address`
-- ----------------------------
DROP TABLE IF EXISTS `user_address`;
CREATE TABLE `user_address` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_address_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user_address
-- ----------------------------
INSERT INTO `user_address` VALUES ('1543819189', null, '3', '张三', '020-81167888', '广东省广州市海珠区新港中路397号', '7');
INSERT INTO `user_address` VALUES ('1544253733', null, '6', '张三', '020-81167888', '广东省广州市海珠区新港中路397号', '1');

-- ----------------------------
-- Table structure for `user_coupon`
-- ----------------------------
DROP TABLE IF EXISTS `user_coupon`;
CREATE TABLE `user_coupon` (
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `coupon_id` int(11) NOT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `coupon_id` (`coupon_id`),
  CONSTRAINT `user_coupon_ibfk_1` FOREIGN KEY (`coupon_id`) REFERENCES `coupon` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user_coupon
-- ----------------------------
INSERT INTO `user_coupon` VALUES (null, null, '1', '1', '1', '1');
INSERT INTO `user_coupon` VALUES (null, null, '2', '1', '2', '1');
