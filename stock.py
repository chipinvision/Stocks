import requests

ticker = input("Enter Ticker: ")
api_key = 'your api key here'

def get_price(ticker_symbol, api):
	url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
	res = requests.get(url).json()
	price = res['price'][:-3]
	return price

def get_name(ticker_symbol, api):
	url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
	res = requests.get(url).json()
	name = res['name']
	return name

def get_data(ticker_symbol, api):
	url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
	res = requests.get(url).json()
	return res

stockname = get_name(ticker,api_key)
stockprice = get_price(ticker,api_key)
stockdata = get_data(ticker,api_key)
exchange = stockdata['exchange']
currency = stockdata['currency']
open = stockdata['open'][:-3]
high = stockdata['high'][:-3]
low = stockdata['low'][:-3]
close = stockdata['close'][:-3]

print("Stock Name: ",stockname)
print("Stock Price: ",stockprice)
print("Exchange: ", exchange)
print("Currency: ",currency)
print("Opening Price: ",open)
print("High Price: ", high)
print("Low Price: ",low)
print("Closing Price: ",close)