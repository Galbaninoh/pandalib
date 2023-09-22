from pandalib import pandalib, pandautilities

utilities = pandautilities(pandabuy_auth, pandabuy_userid)

shipping_prices = utilities.estimate(weight=1200, length=30, hight=30, width = 30)

print(shipping_prices)