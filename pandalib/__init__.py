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
    
    def get_item_skus(self, itemurl:str):
        body = {"urlList": [itemurl]}
        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Opera\";v=\"103\"",
            "Referer": "https://qc.pandabuy.com/search?k=414ea3da4c1e45a6ef7f3585dbe92faf",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        url = f"https://qc.pandabuy.com/gateway/order/getItemSkuListByUrl"
        r = self.session.post(url, json=body, headers=headers)
        return r.json()

    def get_qc_photos(self, itemurl:str, sku:str):
        url = f"https://www.pandabuy.com/gateway/product/itemGet?url={itemurl}&userId={self.userid}"
        header = {"Accept" : "*/*", "Authorization" : "Bearer " + self.auth,"Currency" : "USD", "Referer": "https://qc.pandabuy.com/qc?"}
        r_item = self.session.get(url, headers=header)
        r_item_response = r_item.json()
        goods_id = r_item_response["data"]["item"]["num_iid"]
        url = "https://qc.pandabuy.com/gateway/order/getItemPictureBySku"
        body = {"goodsId": goods_id, "skuId": sku, "pictureType": "0"}
        r = self.session.post(url, json=body, headers=header)
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
