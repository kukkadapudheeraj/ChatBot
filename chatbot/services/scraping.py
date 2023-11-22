import requests,os
from bs4 import BeautifulSoup
import json
import re
import roman
import os
import nltk
import csv
from nltk.corpus import stopwords
nltk.download('stopwords')

class Scraping:

    def __init__(self):
        pass

    def lowerCase(text):
        return text.lower()
    
    def trim_extra_characters(input_string):
        trimmed_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', input_string)
        trimmed_string = re.sub(r'\s+',' ', trimmed_string)
        return trimmed_string
    
    def whitespace_tokenize(input_string):
        temp_list = input_string.split(' ')
        for each_word in temp_list:
            if len(each_word)>0 and each_word!=' ':
                pass
            else:
                temp_list.remove(each_word)
        return temp_list
    
    def trim_stop_words(token_list):
        stopwords_list = stopwords.words('english')
        output_token_list = []
        for word in token_list:
            if word not in stopwords_list and len(word)>0:
                output_token_list.append(word)
        return output_token_list

    def extract_novel_texts(novel_text):
        text_data = novel_text.split('\n')
        tokens=[]
        for each_line in text_data:
            each_line = re.split(r'\t+', each_line.rstrip('\t'))
            line =  each_line.rstrip('\n')
            line = Scraping.lowerCase(line)
            line = Scraping.trim_extra_characters(line)
            tokenized_line = Scraping.whitespace_tokenize(line)
            token_list = Scraping.trim_stop_words(tokenized_line)        
            tokens.extend(token_list)
        return tokens

    def initialize_scraping():
        dataset=[["book_title","paragraph"]] 
        folder_path = os.path.join(os.path.dirname(__file__), '../static/')
        files = os.listdir(folder_path)
        for file in files:
            file = file.rstrip('.txt')
            with open(folder_path+file+'.txt', 'r') as file_reader:
                content = file_reader.read()
            paragraphs = content.split('\n\n')
            for paragraph in paragraphs:
                paragraph = paragraph.strip()
                paragraph = Scraping.trim_extra_characters(paragraph)
                paragraph = Scraping.lowerCase(paragraph)
                if len(paragraph)!=0:
                    row = []
                    row.append(file)
                    row.append(paragraph)
                    dataset.append(row)
        
        csv_file_path = os.path.join(os.path.dirname(__file__), '../dataset.csv')
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in dataset:
                csv_writer.writerow(row)
        pass
                

