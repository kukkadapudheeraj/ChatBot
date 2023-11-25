from chatbot import create_app
from chatbot.services.scraping import Scraping

app = create_app()

if __name__ == '__main__':
   
   # Scraping.initialize_scraping()
   app.run(host='127.0.0.1',port=9999)


