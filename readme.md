## **Objective :**
The objective is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below.

## **Data Extraction :**
For each of the articles, given in the input.xlsx file, extract the article text and save the extracted article in a text file with URL_ID as its file name. While extracting text, please make sure your program extracts only the article title and the article text. It should not extract the website header, footer, or anything other than the article text

## **Data Analysis :**
For each of the extracted texts from the article, performing textual analysis and compute variables, given in the output structure excel file. We need to save the output in the exact order as given in the output structure file, “Output Data Structure.xlsx”Sentimental Analysis
Sentimental analysis is the process of determining whether a piece of writing is positive, negative, or neutral. The below Algorithm is designed for use in Financial Texts. It consists of steps:
- Cleaning using Stop Words Lists
The Stop Words Lists (found in the folder StopWords) are used to clean the text so that Sentiment Analysis can be performed by excluding the words found in Stop Words List.
- Creating a dictionary of Positive and Negative words
The Master Dictionary (found in the folder MasterDictionary) is used for creating a dictionary of Positive and Negative words. We add only those words in the dictionary if they are not found in the Stop Words Lists.

## **Output Variables :**
#### 1. All input variables in “Input.xlsx”
#### 2. POSITIVE SCORE
This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
#### 3. NEGATIVE SCORE
This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
#### 4. POLARITY SCORE
This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula:
Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) +
0.000001)
The range is from -1 to +1
#### 5. SUBJECTIVITY SCORE
This is the score that determines if a given text is objective or subjective. It is calculated by using the formula:
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) +
0.000001)
Range is from 0 to +1
#### 6. AVG SENTENCE LENGTH
Average Sentence Length = the number of words / the number of sentences
#### 7. PERCENTAGE OF COMPLEX WORDS
Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)
#### 8. FOG INDEX
Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)
#### 9. AVG NUMBER OF WORDS PER SENTENCE
Complex words are words in the text that contain more than two syllables.
#### 10. COMPLEX WORD COUNT
Complex words are words in the text that contain more than two syllables.
#### 11. WORD COUNT
We count the total cleaned words present in the text by
1. removing the stop words (using stopwords class of nltk package).
2. removing any punctuations like ? ! , . from the word before counting.
#### 12. SYLLABLE PER WORD
To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the
words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US
is not included in the list.
#### 13. PERSONAL PRONOUNS
To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the
words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US
is not included in the list.
#### 14. AVG WORD LENGTH
Sum of the total number of characters in each word/Total number of words

Checkout output data structure spreadsheet for the format of the output, i.e. “Output Data Structure.xlsx”.
