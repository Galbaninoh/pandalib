from pandalib import pandalib, pandautilities

lib = pandalib("my bearer token", "my user id")

item = lib.get_item("https://item.taobao.com/item.htm?id=634959757581")

print(item)