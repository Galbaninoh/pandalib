from cloudscraper import CloudScraper

class pandalib:
    def __init__(self, auth : str, userid : str):
        self.auth = auth
        self.userid = userid
        self.session = CloudScraper()

    def get_item(self, itemurl:str):
        url = f"https://www.pandabuy.com/gateway/product/itemGet?url={itemurl}&userId={self.userid}"
        header = {"Accept" : "*/*", "Authorization" : "Bearer " + self.auth,"Currency" : "USD"}
        r = self.session.get(url, headers=header)
        return r.json()
    
    def get_balance(self):
        url = f"https://api.pandabuy.com/gateway/pay/wallet/balance"
        header = {"Accept" : "*/*", "Authorization" : "Bearer " + self.auth,"Currency" : "USD"}
        r = self.session.get(url, headers=header)
        return r.json()

    def get_user_info(self):
        url = f"https://api.pandabuy.com/gateway/user/getUserInfo"
        header = {"Accept" : "*/*", "Authorization" : "Bearer " + self.auth,"Currency" : "USD"}
        r = self.session.get(url, headers=header)
        return r.json()
    
    def get_cart(self):
        url = f"https://www.pandabuy.com/gateway/user/cart/allList"
        header = {"Accept" : "*/*", "Authorization" : "Bearer " + self.auth,"Currency" : "USD"}
        r = self.session.get(url, headers=header)
        return r.json()

class pandautilities:
    def __init__(self, auth : str, userid : str):
        self.auth = auth
        self.userid = userid
        self.session = CloudScraper()
    
    def estimate(self, weight : float, length : float = None, hight : float = None, width : float = None):
        body = {
            "countryId": "24",
            "limitArr": [],
            "itemLimitArr": [],
            "storageNo": 13,
            "length": length,
            "width": width,
            "hight": hight,
            "weight": weight,
            "dateRange": None,
            "needTimeLine": True,
            "provinceId": None,
            "province": None,
            "beginTime": None,
            "endTime": None,
            "userId": int(self.userid),
            "vipLevel": 0,
            "checkPermission": True,
            "ignoreDZWL": True,
            "needConfig": True,
            "needInsurance": True
        } 
        url = f"https://www.pandabuy.com/gateway/logistics/estimate"
        header = {"Accept" : "*/*", "Authorization" : "Bearer " + self.auth}
        r = self.session.post(url, headers=header, json=body)
        return r.json()

    def cny_to_usd(self, cny:float):
        url = f"https://www.pandabuy.com/gateway/pay/exchangeRate/rateList"
        header = {"Accept" : "*/*", "Authorization" : "Bearer " + self.auth}
        r = self.session.get(url, headers=header)
        exchangeRate = r.json()["data"][0]["rate"]
        result = round(cny / exchangeRate, 2)
        return result
