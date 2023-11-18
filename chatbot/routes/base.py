from flask import Blueprint,request


base = Blueprint('base',__name__)

@base.route('/execute_query',methods=['GET', 'POST'])
def index():
    pass
   
