import requests,os
from bs4 import BeautifulSoup
import json
import re
import roman
import os
import nltk
import csv
from nltk.corpus import stopwords
from chatbot.services.classifier import Classifier
from chatbot.services.retrieval import Retrieval
from chatbot.services.data_loading import DataLoading
from chatbot.services.chitchat import Chitchat
nltk.download('stopwords')
import pickle
# vectorizer,classifier = Classifier.define_classifier()
novel_vectorizer,novel_classifier = Classifier.define_novel_classifier()
path = os.path.join(os.path.dirname(__file__), './naive_bayes/')
with open(path+'naive_bayes_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
with open(path+'naive_bayes_vectorizer.pkl', 'rb') as file:
    loaded_vectorizer = pickle.load(file)

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
    
    def trim_stop_words(paragraph):
        stopwords_list = stopwords.words('english')
        words_list = paragraph.split(' ')
        output_word_list = []
        for word in words_list:
            if word not in stopwords_list and len(word)>0:
                output_word_list.append(word)
        paragraph = " ".join(output_word_list)
        return paragraph

    def dataset_preparation():
        novel_dataset=[["book_title","paragraph"]] 
        classifier_dataset=[["query_type","text"]]
        actual_docs = [["book_title","paragraph"]]
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
                actual_docs.append([file,paragraph])
                paragraph = Scraping.trim_stop_words(paragraph)
                if len(paragraph)!=0:
                    row = []
                    another_row=[]
                    row.append(file)
                    row.append(paragraph)
                    novel_dataset.append(row)
                    another_row.append("novel")
                    another_row.append(paragraph)
                    classifier_dataset.append(another_row)
        csv_file_path = os.path.join(os.path.dirname(__file__), '../chitchat_conversations1.csv')
        with open(csv_file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                title,text = row
                if(title == "query_type"):
                    continue
                if(len(text)>0):
                    classifier_dataset.append([title,text])
        csv_file_path = os.path.join(os.path.dirname(__file__), '../novel_dataset.csv')
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in novel_dataset:
                csv_writer.writerow(row)
        csv_file_path = os.path.join(os.path.dirname(__file__), '../docs_dataset.csv')
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in actual_docs:
                csv_writer.writerow(row)
        csv_file_path2 = os.path.join(os.path.dirname(__file__), '../classifier_dataset.csv')
        with open(csv_file_path2, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in classifier_dataset:
                csv_writer.writerow(row)
        
    def initialize_chatting(question,query_type,novel_name):

        try:
            topic_name = novel_name
            if query_type == "novel":
                if novel_name=="":
                    novel_user_input_tfidf = novel_vectorizer.transform([question])
                    novel_predicted_genre = novel_classifier.predict(novel_user_input_tfidf)
                    genre = novel_predicted_genre[0]
                    topic_name = genre
                else:
                    genre = novel_name
                genre = DataLoading.to_snake_case(genre)
                print(genre)
                answer = Retrieval.generate_answer(question,genre)
                answer = Scraping.trim_extra_characters(answer)
                return answer,topic_name
            elif query_type == "chitchat":
                topic_name=query_type
                response = Chitchat.chat(question)
                return response,topic_name
            else:
                # Scraping.dataset_preparation()
                # user_input_tfidf = vectorizer.transform([question])
                # predicted_genre = classifier.predict(user_input_tfidf)
                query_cleaned = question.replace("[^a-zA-Z]", " ").lower()
                query_tfidf = loaded_vectorizer.transform([query_cleaned])
                predicted_genre = loaded_model.predict(query_tfidf)
                print(predicted_genre[0])
                if predicted_genre[0]=="novel":
                    novel_user_input_tfidf = novel_vectorizer.transform([question])
                    novel_predicted_genre = novel_classifier.predict(novel_user_input_tfidf)
                    genre = novel_predicted_genre[0]
                    topic_name = genre
                    genre = DataLoading.to_snake_case(genre)
                    print(genre)
                    answer = Retrieval.generate_answer(question,genre)
                    answer = Scraping.trim_extra_characters(answer)
                    return answer,topic_name
                else:
                    topic_name = "chitchat"
                    response = Chitchat.chat(question)
                    return response,topic_name
        except Exception as e:
            pass
        
                

