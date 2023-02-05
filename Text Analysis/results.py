import codecs
import os
import pandas as pd
import openpyxl
import nltk
import re

#No. of modified text files 
folder_path = 'C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Modified txt files\\'
files = os.listdir(folder_path)
count_f = 0
for file in files:
    if file.endswith('.txt'):
        count_f += 1

#Open Excel file where results to be written
wb = openpyxl.load_workbook('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Results\\Output Data Structure.xlsx')
sheet = wb['Sheet1']

#Excessing Input.xlsx for URL_ID
df = pd.read_excel('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Data Extraction\\Input.xlsx',sheet_name='Sheet1',usecols=['URL_ID','URL'])

for i in range(count_f):
    filename = df.iloc[i,0]
    filename = str(filename)
    path='C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Modified txt files\\'+filename+'_new.txt'
    # No. of Words and Complex words in Modified text file
    with codecs.open(path, 'r',encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        # Words count
        num_words = len(words)
        # Character count
        num_characters = 0
        for ch in text:
            if ch.isalpha() or ch.isdigit():
                num_characters += 1
        # Complex Words count
        pattern = r'[aeiou]{2,}' 
        complex_words = []
        for word in words:
            if re.search(pattern, word):
                complex_words.append(word)
        num_comp_words = len(complex_words)
        #syllable count
        num_syllables = 0
        for word in words:
            word = re.sub(r'[^a-zA-Z]', '', word)
            word = word.lower()
            num_vowels = len(re.findall(r'[aeiou]', word))
            num_vowels -= len(re.findall(r'(?:^[aeiou]e|[aeiou]es|[aeiou]ed|[aeiou]ing)$', word))
            num_syllables += num_vowels
    # No. of sentence in extracted text file
    path1='C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Data Extraction\\Extracted data txt files\\'+filename+'.txt'
    with codecs.open(path1, 'r',encoding='utf-8') as file:
        text_s = file.read()
        sentences = nltk.sent_tokenize(text_s)
        #Sentence count
        num_sentences = len(sentences)

    #Positive and Negative word count
    with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Master Dictionary\\positive-words.txt', 'r') as file:
        positive_words = file.read()
    with open('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Master Dictionary\\negative-words.txt', 'r') as file:
        negative_words = file.read()
    # Split the contents of the file into a list of positive words
    negative_words = negative_words.split()
    positive_words = positive_words.split()
    # Initialize the count to zero
    count_p = 0
    count_n = 0
    # Loop through the words in the modified text file to count p and n 
    for word in words:
        if word in positive_words:
            count_p += 1

    for word in words:
        if word in negative_words:
            count_n += 1  
    
    #personal pronoun count
    path2='C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Data Extraction\\Extracted data txt files\\'+filename+'.txt'
    with codecs.open(path2, 'r',encoding='utf-8') as file:
        text_p = file.read()
        pattern = r"\b(?:I|we|my|ours|us)\b"
        matches = re.findall(pattern, text_p)
        p_len=len(matches)


    #Writing results        
    sheet[f'C{i + 2}']=count_p
    sheet[f'D{i + 2}']=count_n
    sheet[f'E{i + 2}']=(count_p-count_n)/(count_p+count_n+0.000001)
    sheet[f'F{i + 2}']=(count_p+count_n)/(num_words+0.000001)
    sheet[f'G{i + 2}']=num_words/num_sentences
    sheet[f'H{i + 2}']=num_comp_words/num_words
    sheet[f'I{i + 2}']=0.4*((num_words/num_sentences)+(num_comp_words/num_words))
    sheet[f'J{i + 2}']=num_words/num_sentences #Doubt 
    sheet[f'K{i + 2}']=num_comp_words
    sheet[f'L{i + 2}']=num_words
    sheet[f'M{i + 2}']=num_syllables
    sheet[f'N{i + 2}']=p_len
    sheet[f'O{i + 2}']=num_characters/num_words
    sheet[f'P{i + 2}']=i

    print(i)
    
    wb.save('C:\\Users\\HP\\Desktop\\BlackCoffer Assignment\\Text Analysis\\Results\\Output Data Structure.xlsx')