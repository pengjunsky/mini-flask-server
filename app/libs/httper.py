import requests


class Http:
    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)
        if res.status_code != 200:
            return {} if return_json else ''
        return res.json() if return_json else res.text

    @staticmethod
    def post(url, data, headers, return_json=True):
        if not headers:
            headers = {'Content-Type': 'application/json'}
        res = requests.post(url, data=data.encode(), headers=headers)
        res.encoding = 'utf-8'
        if res.status_code != 200:
            return {} if return_json else ''
        return res.json() if return_json else res.text
