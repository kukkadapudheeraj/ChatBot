import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os
class Classifier:

    def __init__(self):
        pass
    
    def train_classifier():
        pass
    
    def define_classifier():
        file_path = os.path.join(os.path.dirname(__file__), '../classifier_dataset.csv')
        df = pd.read_csv(file_path)  
        X = df['text']
        y = df['query_type']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        vectorizer = TfidfVectorizer()
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)
        classifier = LogisticRegression(max_iter=1000)
        classifier.fit(X_train_tfidf, y_train)
        predictions = classifier.predict(X_test_tfidf)
        accuracy = accuracy_score(y_test, predictions)
        # print(f"Accuracy: {accuracy:.2f}")
        # print("Classification Report:\n", classification_report(y_test, predictions))
        return vectorizer,classifier
        # while True:
        #     user_input = input("Enter a paragraph summary for book_title classification: ")
        #     user_input_tfidf = vectorizer.transform([user_input])
        #     predicted_genre = classifier.predict(user_input_tfidf)
        #     print(f"Predicted Genre: {predicted_genre[0]}")
        # pass


    def define_novel_classifier():
        file_path = os.path.join(os.path.dirname(__file__), '../novel_dataset.csv')
        df = pd.read_csv(file_path)  
        X = df['paragraph']
        y = df['book_title']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        vectorizer = TfidfVectorizer()
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)
        classifier = LogisticRegression(max_iter=1000)
        classifier.fit(X_train_tfidf, y_train)
        predictions = classifier.predict(X_test_tfidf)
        accuracy = accuracy_score(y_test, predictions)
        # print(f"Accuracy: {accuracy:.2f}")
        # print("Classification Report:\n", classification_report(y_test, predictions))
        return vectorizer,classifier


