# import modules
import urllib.request
import nltk
import re 
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer

# define function to remove digits from a string
def remove(list): 
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list] 
    return list

# Gather Book of Genesis Text from website
response =  urllib.request.urlopen('http://www.vatican.va/archive/bible/genesis/documents/bible_genesis_en.html')
html = response.read()

# Convert the text from html to text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)

# Remove punctuation
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)
tokens_ = remove(tokens)
  
# Remove all English stopwords
stop_words = set(stopwords.words('english')) 
filtered_sentence = [w for w in tokens_ if not w in stop_words] 
filtered_sentence = [] 
for w in tokens_: 
    if w not in stop_words: 
        filtered_sentence.append(w) 

# Plot a frequency distribution of the most commonly used words
freq = nltk.FreqDist(filtered_sentence)
#for key,val in freq.items():
#    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)