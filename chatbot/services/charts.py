
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from io import BytesIO
import base64
import json,os
from flask import Flask,render_template
charts_data_path = os.path.join(os.path.dirname(__file__), './charts_data.json')
with open(charts_data_path, 'r') as file:
    charts_data = json.load(file)


charts_images = os.path.join(os.path.dirname(__file__), '../static/images')
class Charts:

    def __init__():
        pass

    def query_length_vs_time():
        x = charts_data["query_length_vs_time"]["length"]
        y = charts_data["query_length_vs_time"]["time"]
        plt.bar(x, y, label='Query Length vs Time')
        plt.xlabel('Query Length')
        plt.ylabel('Time')
        plt.title('Query Length vs Time')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        image_path = os.path.join(charts_images, 'query_length_vs_time.png')
        plt.savefig(image_path, format='png')
        plt.close()
        pass

    def topic_vs_relevance():
        topic_names = charts_data["topic_vs_relevance"].keys()
        values = charts_data["topic_vs_relevance"].values()
        plt.bar(topic_names, values, color='skyblue', edgecolor='black')
        plt.xlabel('Topic Names') 
        plt.ylabel('Relevance Score')       
        plt.title('Topic Vs Relevance Scores')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        image_path = os.path.join(charts_images, 'topic_vs_relevance.png')
        plt.savefig(image_path, format='png')
        plt.close()
        pass
        

    def topic_vs_number_of_queries():
        topic_names = charts_data["topic_vs_number_of_queries"].keys()
        values = charts_data["topic_vs_number_of_queries"].values()
        plt.bar(topic_names, values, color='skyblue', edgecolor='black')
        plt.xlabel('Topic Names') 
        plt.ylabel('Number of Queries')       
        plt.title('Topic Vs Number of Queries')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        image_path = os.path.join(charts_images, 'topic_vs_number_of_queries.png')
        plt.savefig(image_path, format='png')
        plt.close()
        pass

    def relevance_vs_non_relevance():
        labels = ["relevant", "non-relevant"]
        relevant = charts_data["relevance_vs_non_relevance"]["relevant"]
        non_relevant = charts_data["relevance_vs_non_relevance"]["non-relevant"]
        relevant_percent = (relevant*100)/(relevant+non_relevant)
        non_relevant_percent = (non_relevant*100)/(relevant+non_relevant)
        sizes = [relevant_percent,non_relevant_percent]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Relevance vs Non-relevance')
        image_path = os.path.join(charts_images, 'relevance_vs_non_relevance.png')
        plt.savefig(image_path, format='png')
        plt.close()
        pass

    
# Charts.topic_vs_relevance()
# Charts.query_length_vs_time()
# Charts.topic_vs_number_of_queries()