from pandalib import pandalib, pandautilities

lib = pandalib("my bearer token", "my user id")

cart = lib.get_cart()

print(cart)