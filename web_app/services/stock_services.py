# Place that will be used to get the 
# stock info

import requests , json


# Doing a "GET" request
symbol = "DIS"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min"
key = {"apikey": "abc123"}
# now putting that into the request with the reqeusts package
r = requests.get(url=url, params=key)


# converting the string into a json object
