from pandalib import pandalib, pandautilities

utilities = pandautilities("my bearer token", "my user id")

usd = utilities.cny_to_usd(230)

print(usd)