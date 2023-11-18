import requests,os
from bs4 import BeautifulSoup
import json

urls = ['https://www.gutenberg.org/files/1661/1661-h/1661-h.htm',
        'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm',
        'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm',
        'https://www.gutenberg.org/files/98/98-h/98-h.htm',
        'https://www.gutenberg.org/files/11/11-h/11-h.htm',
        'https://www.gutenberg.org/files/345/345-h/345-h.htm',
        'https://www.gutenberg.org/files/84/84-h/84-h.htm',
        'https://www.gutenberg.org/files/74/74-h/74-h.htm',
        'https://www.gutenberg.org/files/768/768-h/768-h.htm',
        'https://www.gutenberg.org/files/174/174-h/174-h.htm']


class Scraping:

    def __init__(self):
        pass


    

    def scrape_data(url):
        count = 1
        docs_file = os.path.join(os.path.dirname(__file__), '../static/')
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to retrieve the page")
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            title = soup.find('h1').text.strip()
            author = soup.find('span', itemprop='name').text.strip()
            content = soup.find('div', class_='chapter')
            content_text = content.text.strip() if content else "Content not found"
            book_data = {
            'title': title,
            'author': author,
            'content': content_text
            }
            with open(docs_file+title+'.json', 'w', encoding='utf-8') as file:
                json.dump(book_data,file, indent=4)
            print(count,"Book downloaded successfully")
            count = count+1
        pass


    def initialize_scraping():
        
        for each_url in urls:
            Scraping.scrape_data(each_url)
