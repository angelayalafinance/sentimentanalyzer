from itertools import count
from xml.etree.ElementTree import tostringlist
from numpy import array
from pandas import read_csv

#   Import positive word dictionary
positive = read_csv('/Users/angel/Downloads/Loughran_Mcdonald_word_list/LoughranMcDonald_Positive.csv', delimiter = ',')

#   convert words to lowercase
positive = positive.values.ravel().tolist()

for i in range(len(positive)):
    positive[i] = positive[i].lower()



# Populate a list of file paths
path = ('/Users/angel/Downloads/amgen1.rtf')





#   Function that parses word file into a words
def filereader(path):
    array = []
    article = open(path, 'r')
    for words in article.read().split():
        array.append(words)
    return array
    

#   Function that counts number of positive words, passing word file array
def scorecount(arr):
    score = 0
    for i in arr:
        score += positive.count(i)
    return score



#   Create a company class object
class Stock:
  def __init__(self, name, ticker, score, performance, path):
    #
    #
    #
    #

#   Store class objects in a list


#   Iteratively update stock score
arr = []
for company in path:
    arr = filereader(path)
    sentimentscore = scorecount(arr)

    
#   Calculate stock performance    
    
    
    
    
#   Import old stock portfolio




#   Compare performance
