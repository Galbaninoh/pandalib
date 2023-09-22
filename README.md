
# Pandalib

A python module to get informations from the api of the popular agent Pandabuy


## Installation

Install the package using pip

```bash
  pip install pandalib
```
Since Pandabuy requires login for basically every api request you will need your pandabuy bearer token and your userid

### Get your bearer token and user id
You can get your bearer token from the headers of any api request

![Imgur Image](https://i.imgur.com/uBCdo0Q.png)

You can get your user id from the profile info

![Imgur Image](https://i.imgur.com/mdoJsW0.png)


## Usage/Examples

### Get an item info

```python
from pandalib import pandalib, pandautilities

lib = pandalib("my bearer token", "my user id")

item = lib.get_item("https://item.taobao.com/item.htm?id=634959757581")

print(item)
```

### Get your account balance

```python
from pandalib import pandalib, pandautilities

lib = pandalib("my bearer token", "my user id")

balance = lib.get_balance()

print(balance)
```

### Get your account info

```python
from pandalib import pandalib, pandautilities

lib = pandalib("my bearer token", "my user id")

info = lib.get_user_info()

print(info)
```

### Get your account cart

```python
from pandalib import pandalib, pandautilities

lib = pandalib("my bearer token", "my user id")

cart = lib.get_cart()

print(cart)
```

## Pandautilities

You can use pandautilities to estimate the shipping prices and convert cny to usd

### Convert CNY to USD 

```python
from pandalib import pandalib, pandautilities

utilities = pandautilities("my bearer token", "my user id")

usd = utilities.cny_to_usd(230)

print(usd)
```

### Estimate shipping prices

To estimate the shipping prices you can only input the weight or you can also input width, hight, length

```python
from pandalib import pandalib, pandautilities

utilities = pandautilities("my bearer token", "my user id")

shipping_prices = utilities.estimate(weight=1200, length=30, hight=30, width = 30)

print(shipping_prices)
```
