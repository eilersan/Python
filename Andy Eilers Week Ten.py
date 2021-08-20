"""
Author: Andy Eilers
Created 8/16/2021
Purpose: Input and adjust stock value data analytics of trade scenarios
"""

from datetime import datetime
import matplotlib.pyplot as plt
import json
import matplotlib

#importing files
stocks_file = r'C:\Users\andy.eilers\Downloads\Lesson6_Stocks.csv'
file_path = r'C:\Users\andy.eilers\Downloads/AllStocks.json'
with open(file_path) as json_file:
    data_set = json.load(json_file)

#getting stocks information
try:
    read_file = open(stocks_file, 'r')
except FileNotFoundError:
    print("The Stocks file is not here")

header = read_file.readline()
header = header.strip('\n')
header_split = header.split(',')
symbol_index = header_split.index('SYMBOL')
shares_index = header_split.index('NO_SHARES')
price_index = header_split.index('PURCHASE_PRICE')
value_index = header_split.index('CURRENT_VALUE')
date_index = header_split.index('PURCHASE_DATE')

#trade class

class Stock():
    def __init__(self, symbol, date, open_price, high, low, close_price, volume):
        self.symbol = symbol
        self.date = date
        self.open_price = open_price
        self.high = high
        self.low = low
        self.close = close_price
        self.volume = volume
        self.share_list = []
        self.date_valued = []

    def find_change(self, symbol, open_price, close_price):
        self.find_change.append(symbol, close_price - open_price)
    def add_dates(self, symbol, date):
        self.date_valued.append(symbol, date)


#value Dictionary
stockDictionary = {}

for stock in data_set:
    if stock['Symbol'] not in stockDictionary:
        newStock = Stock(stock['Symbol'], stock['Date'], stock['Open'], stock['High'], stock['Low'],
                         stock['Close'], stock['Volume'])
        print(stock['Symbol'] + " added")
        stockDictionary[stock['Symbol']] = newStock
    else:
        stockDictionary[stock['Date']].date = stock['Date']

    stockDictionary[stock['Symbol']].find_change(
        stock['Date'], ['Open'], ['Close'])

#creating chart
plt.title = 'Daily Change in Value by Symbol'
plt.xlabel = 'Date'
plt.ylabel = 'Amount of Change'

for date in stockDictionary:
    amount = stockDictionary[stock].find_change
    date = stockDictionary[stock].date
    stock = stockDictionary[stock].symbol
    plt.plot_date(date, amount, linestyle='solid', label='Stock')

plt.legend()
plt.show()
plt.savefig('simplePlot.png')