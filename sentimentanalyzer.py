from itertools import count
from xml.etree.ElementTree import tostringlist
from numpy import array
from pandas import read_csv
import yfinance as yf
import pandas as pd
import numpy as np
#   Import positive word dictionary
positive = read_csv('/Users/angel/Downloads/Loughran_Mcdonald_word_list/LoughranMcDonald_Positive.csv', delimiter = ',')

#   convert words to lowercase
positive = positive.values.ravel().tolist()

for i in range(len(positive)):
    positive[i] = positive[i].lower()


# Populate a list of file paths file documents for each of the 30 companies on the DOW


companies = {
    'AXP' : '/Users/angel/Downloads/newsdocs/Amex.RTF',
    'AMGN' : '/Users/angel/Downloads/newsdocs/amgen1.RTF',
    'AAPL' : '/Users/angel/Downloads/newsdocs/Apple.RTF',
    'BA' : '/Users/angel/Downloads/newsdocs/Boeing.RTF',
    'CAT' : '/Users/angel/Downloads/newsdocs/Caterpillar.RTF',
    'CSCO' : '/Users/angel/Downloads/newsdocs/Cisco.RTF',
    'CVX' : '/Users/angel/Downloads/newsdocs/Chevron.RTF',
    'GS' : '/Users/angel/Downloads/newsdocs/GoldmanSachs.RTF',
    'HD' : '/Users/angel/Downloads/newsdocs/HomeDepot.RTF',
    'HON' : '/Users/angel/Downloads/newsdocs/Honeywell.RTF',
    'IBM' : '/Users/angel/Downloads/IBM.RTF',
    'INTC' : '/Users/angel/Downloads/newsdocs/Intel.RTF',
    'JNJ' : '/Users/angel/Downloads/newsdocs/Johnson.RTF',
    'KO' : '/Users/angel/Downloads/newsdocs/Coke.RTF',
    'JPM' : '/Users/angel/Downloads/newsdocs/JPMC.RTF',
    'MCD' : '/Users/angel/Downloads/newsdocs/Mcdonalds.RTF',
    'MMM' : '/Users/angel/Downloads/newsdocs/3m.RTF',
    'MRK' : '/Users/angel/Downloads/newsdocs/Merck.RTF',
    'MSFT' : '/Users/angel/Downloads/newsdocs/Microsoft.RTF',
    'NKE' : '/Users/angel/Downloads/newsdocs/Nike.RTF',
    'PG' : '/Users/angel/Downloads/newsdocs/PG.RTF',
    'TRV' : '/Users/angel/Downloads/newsdocs/Travelers.RTF',
    'UNH' : '/Users/angel/Downloads/newsdocs/UnitedHealth.RTF',
    'CRM' : '/Users/angel/Downloads/newsdocs/Salesforce.RTF',
    'VZ' : '/Users/angel/Downloads/newsdocs/Verizon.RTF',
    'V' : '/Users/angel/Downloads/newsdocs/Visa.RTF',
    'WBA' : '/Users/angel/Downloads/newsdocs/Walgreens.RTF',
    'WMT' : '/Users/angel/Downloads/newsdocs/Walmart.RTF',
    'DIS' : '/Users/angel/Downloads/Disney.RTF',   
    'DOW' : '/Users/angel/Downloads/newsdocs/Dow.RTF'
    }


#   Function that parses word file into a words and stores them into a list
def filereader(values):
    wordlist = []
    article = open(values, 'r')
    for words in article.read().split():
        wordlist.append(words)
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].lower()
    return wordlist

#   Function that counts number of positive words, passing word file list
def scorecount(arr):
    score = 0
    for i in arr:
        score += positive.count(i)
    return score


#   Stores sentiment scores into a list
list = []
for values in companies.values():
    arr = filereader(values)
    sentimentscore = scorecount(arr)
    list.append(sentimentscore)

#   D
data = pd.DataFrame(companies.keys(), columns = ['Ticker'])
data['Score'] = np.array(list)
data

#Return the 5 stocks with the highest sentiment scores
portfolio =  data.loc[data['Score'] >= 101]
portfolio

#Retrieve pricing data for each security from Yahoo finance
stock_data = yf.download(portfolio['Ticker'].tolist(), start="2021-12-01", end="2022-03-30")


stock_prices = stock_data['Adj Close']
stock_prices = stock_prices.resample("1M").last()
returns = stock_prices.pct_change()
returns.name = "Asset"
















#   Import old stock portfolio




#   Compare performance

#sentiment_portfolio = ['AAPL'....]   top 5 stocks from the sentiment analyzer

old_portfolio = ['AAPL', 'DIS', 'JPM', 'MSFT', 'HD']



#Portfolio Dataframe
#name   #ticker  #shares    #recent closing price   




#   Function that calculates returns 
def return_on_portfolio(portfolio, composition):
    for stock in portfolio:
        #   price = yf.close


    #Stock price today compared to start of project
    #Calculate return on portfolio



