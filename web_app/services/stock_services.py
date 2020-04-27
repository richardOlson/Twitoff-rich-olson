# Place that will be used to get the 
# stock info

import requests , json
import os
import re
from dotenv import load_dotenv

# loading the env variables
load_dotenv()


# Doing a "GET" request
symbol = "DIS"
url_5min = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min"
url_daily  = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}"
SECRET_KEY = os.getenv("ALPHA_VANTAGE_KEY")  
key = {"apikey": SECRET_KEY}
# now putting that into the request with the reqeusts package
r = requests.get(url=url_daily, params=key)


# converting the string into a json object
the_dict = json.loads(r.text)

# Getting the date from the metadata
date = the_dict["Meta Data"]["3. Last Refreshed"]

# Pulling out the string out of the metadata
date = re.match(r"([^\s]+)", date)

latest_close = the_dict['Time Series (Daily)'][date.group()]['4. close']

print(f"The latest closing price for the {symbol} is {latest_close}")