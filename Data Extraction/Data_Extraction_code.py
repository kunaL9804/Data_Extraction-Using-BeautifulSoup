from bs4 import BeautifulSoup
import requests
import pandas as pd
import codecs

#Access input.xlsx file data
df = pd.read_excel("C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Data Extraction\\Input.xlsx",sheet_name='Sheet1',usecols=['URL_ID','URL'])

# Count no. of rows
t=df[df.columns[0]].count()

#Loop starts
for i in range(t):
    url=df.iloc[i,1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup=BeautifulSoup(response.text, 'html.parser')
    title = soup.title.get_text()
    paragraphs = soup.find_all('p')

    #New file created
    filename = df.iloc[i,0]
    filename = str(filename)
    path='C:\\Users\HP\Desktop\\BlackCoffer Assignment\\Data Extraction\\Extracted data txt files\\'+filename+'.txt'
    #Open the file
    file_obj = codecs.open(path, "w", encoding='utf-8')
    #Write extracted data
    file_obj.write(title)   #Title name
    for paragraph in paragraphs: #Title text
        file_obj.write(paragraph.get_text())
    file_obj.seek(0)
    file_obj.close()