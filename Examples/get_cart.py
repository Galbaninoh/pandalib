from pandalib import pandalib, pandautilities

lib = pandalib("my bearer token", "my user id")

balance = lib.get_cart()

print(balance)