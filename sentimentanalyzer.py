






#   Function that parses file into words, passing the file as the argument
from numpy import array


def filereader(articles):
    with open(articles) as file:
    # reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split():
   
          #populate into an array

#   Function that counts number of positive words, passing word file array
def scorecount(arr):
    for i in array:
        # compare word with words
            # increment count

        # return integer







#   Choose the top 5 stocks
