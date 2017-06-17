# First example
# How to install googlefinance package
# Reference: https://pypi.python.org/pypi/googlefinance
# pip install googlefinance
from googlefinance import getQuotes
import json
symbol = 'BBL'        
print(json.dumps(getQuotes('SET:' + symbol), indent=2)) # for Stock of Thailand, There is a prefix with 'SET:'

# Second example
# How to install quandl package
# https://github.com/quandl/quandl-python
# pip install quandl
import quandl
quandl.ApiConfig.api_key = 'hGjH3Bsv8czZQBB515hE' #(your api that must register at https://www.quandl.com/)
data = quandl.get("THAISE/INDEX")
#data = quandl.get("THAISE/INDEX", authtoken="hGjH3Bsv8czZQBB515hE")
print(data.head())

data = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")
print(data.head())


# Third example 
# How to install yahoo_finance package
# Reference: https://pypi.python.org/pypi/yahoo-finance
# pip install yahoo_finance
from yahoo_finance import Share
yahoo = Share("++++YHOO++++")
print("\n++++YHOO stock++++")
print (yahoo.get_open())
print (yahoo.get_price())
print (yahoo.get_trade_datetime())

from yahoo_finance import Currency
eur_pln = Currency('EURPLN')
print("\n++++Currency of EURPLN++++")
print (eur_pln.get_bid())
print (eur_pln.get_ask())
print (eur_pln.get_rate())
print (eur_pln.get_trade_datetime())


# Forth example
# How to install pandas-datareader package
# Reference: https://github.com/pydata/pandas-datareader
# pip install pandas-datareader

# But does't work, It has some bug
# Fix bug: https://github.com/ranaroussi/fix-yahoo-finance (The feature, I think that the bug is solved)
# pip install fix_yahoo_finance --upgrade --no-cache-dir
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf # <== that's all it takes :-)

# If you Stock of Thailand, the symbol must be following '.BK'
# download dataframe
ptt = pdr.get_data_yahoo("PTT.BK", start="2017-01-01", end="2017-04-30")
print()
print(ptt.tail())

