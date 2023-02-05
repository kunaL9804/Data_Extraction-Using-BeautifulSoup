import nltk
import pandas as pd
import codecs
import re
import codecs

stopwords=[]
# Load the Stopwords from a file
with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Stopwords\\StopWords_Auditor.txt', 'r') as file:
    stopwords=file.read().split()
with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Stopwords\\StopWords_Currencies.txt', 'r') as file:
    stopwords=file.read().split()
with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Stopwords\\StopWords_DatesandNumbers.txt', 'r') as file:
    stopwords=file.read().split()
with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Stopwords\\StopWords_Generic.txt', 'r') as file:
    stopwords=file.read().split()
with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Stopwords\\StopWords_GenericLong.txt', 'r') as file:
    stopwords=file.read().split()
with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Stopwords\\StopWords_Geographic.txt', 'r') as file:
    stopwords=file.read().split()
with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Stopwords\\StopWords_Names.txt', 'r') as file:
    stopwords=file.read().split()

# Create a custom stopwords list
custom_stopwords = nltk.corpus.stopwords.words() + stopwords
#Read URL_ID for accessing files(as it has same name)
df = pd.read_excel('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Data Extraction\\Input.xlsx',sheet_name='Sheet1',usecols=['URL_ID','URL'])
t=df[df.columns[0]].count()

for i in range(t):
    filename = df.iloc[i,0]
    filename = str(filename)
    path='C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Data Extraction\\Extracted data txt files\\'+filename+'.txt'
    with codecs.open(path, 'r',encoding='utf-8') as file:
        text = file.read()
    # Remove unwanted characters
    text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    text=re.sub(r"(@\[A-Za-z0-9]+) | ([^0-9A-Za-z \t]) | (\w+:\/\/\S+) | ^rt | http.+?"," ",text.lower())

    # Lowercase the text
    text = text.lower()

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove the stopwords
    filtered_tokens = [token for token in tokens if token not in custom_stopwords]

    # Open the file in write mode
    path='C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Modified txt files\\'+filename+'_new.txt'
    with codecs.open(path, 'w', encoding='utf-8') as file:
        # Write each element of the list to a separate line
        for element in filtered_tokens:
            file.write(element+" ")
