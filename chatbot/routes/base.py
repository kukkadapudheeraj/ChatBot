from flask import Blueprint,request,render_template
from chatbot.services.scraping import Scraping
from chatbot.services.charts import Charts
from flask_cors import cross_origin
import time
import os,json
base = Blueprint('base',__name__)

@base.route('/execute_query',methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def index():
    if request.method == 'GET':
        return "Hello , Hope you are doing great... !! Please use POST method to get valid results"
    elif request.method == 'POST':
        charts_data_path = os.path.join(os.path.dirname(__file__), '../services/charts_data.json')
        with open(charts_data_path, 'r') as file:
            charts_data = json.load(file)
        start_time = time.time()
        question = request.json["question"]
        query_length = len(question)
        query_type = request.json["query_type"]
        novel_name = request.json["novel_name"]
        answer,topic = Scraping.initialize_chatting(question,query_type,novel_name)
        time_taken =  time.time() - start_time
        charts_data["query_length_vs_time"]["length"].append(query_length)
        charts_data["query_length_vs_time"]["time"].append(time_taken)
        charts_data["topic_vs_number_of_queries"][topic] = charts_data["topic_vs_number_of_queries"][topic]+1
        with open(charts_data_path, 'w') as file:
            json.dump(charts_data, file, indent=2)
        response = {"answer":answer,"topic":topic} 
        return response
   

@base.route('/analysis',methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def analysis():
    if request.method == 'GET':
        Charts.query_length_vs_time()
        Charts.topic_vs_relevance()
        Charts.topic_vs_number_of_queries()
        Charts.relevance_vs_non_relevance()
        return render_template('charts.html')
    
    elif request.method == 'POST':
        return "Hello , Hope you are doing great... !! Please use GET method to get valid results"


@base.route('/relevance',methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def relevance_feedback():
    if request.method == 'POST':
        charts_data_path = os.path.join(os.path.dirname(__file__), '../services/charts_data.json')
        with open(charts_data_path, 'r') as file:
            charts_data = json.load(file)
        relevant = request.json["relevant"]
        topic_name = request.json["topic_name"]
        if relevant == 1:
            charts_data["relevance_vs_non_relevance"]["relevant"] = charts_data["relevance_vs_non_relevance"]["relevant"]+1
            charts_data["topic_vs_relevance"][topic_name] = charts_data["topic_vs_relevance"][topic_name]+1
        else:
            charts_data["relevance_vs_non_relevance"]["non-relevant"] = charts_data["relevance_vs_non_relevance"]["non-relevant"]+1
        with open(charts_data_path, 'w') as file:
            json.dump(charts_data, file, indent=2)
        return {"updated":True}
    elif request.method == 'GET':
        return "Hello , Hope you are doing great... !! Please use GET method to get valid results"
