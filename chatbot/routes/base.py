from flask import Blueprint,request
from chatbot.services.scraping import Scraping
from flask_cors import cross_origin

base = Blueprint('base',__name__)

@base.route('/execute_query',methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def index():
    if request.method == 'GET':
        return "Hello , Hope you are doing great... !! Please use POST method to get valid results"
    elif request.method == 'POST':
        question = request.json["question"]
        query_type = request.json["query_type"]
        answer = Scraping.initialize_chatting(question,query_type)
        response = {"answer":answer} 
        return response
   
