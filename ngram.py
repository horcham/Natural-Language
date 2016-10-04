from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator
def cleanInput(input):
    input = re.sub('\n+',' ',input)     #'\n' to ' '
    input = input.lower()         #to lower
    input = re.sub(' +',' ',input)
    input = bytes(input,'UTF-8')     
    input = input.decode('ascii','ignore')     #decode in ascii, ignore when error 
    cleaninput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation) # remove punctuation on both sides
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i')
            cleaninput.append(ltem)
    return cleaninput

def ngrams(input,n):
    input = cleaninput(input)
    output = []
    for i in range(len(input)-n+1):
        ngramtem = ' '.join(input[i:i+n])
        if ngramtem not in output:
            output[ngramtem] = 0
        output[ngramtem] += 1
    return output
    
    
content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(),'utf-8')
ngrams = ngrams(content,2)
sortedngrams = sorted(ngrams.items(),key=operator.itemgetter(1))
    