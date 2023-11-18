import requests,os
from bs4 import BeautifulSoup
import json
import re

books = [1661,
        1342,
        2701,
        98,
        11,
        345,
        84,
        74,
        768,
        174]


class Scraping:

    def __init__(self):
        pass


    

    def scrape_data(book_id):
        url = 'https://www.gutenberg.org/ebooks/'+str(book_id)+'.txt.utf-8'
        docs_file = os.path.join(os.path.dirname(__file__), '../static/')
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the text content
            txt_content = response.text

            title_pattern = re.compile(r'Title: (.+)', re.IGNORECASE)
            author_pattern = re.compile(r'Author: (.+)', re.IGNORECASE)
            release_date_pattern = re.compile(r'Release date: (.+)', re.IGNORECASE)
            language_pattern = re.compile(r'Language: (.+)', re.IGNORECASE)
            content_start_pattern =  re.compile(r'(?:Chapter|Letter)\s+\d+', re.IGNORECASE)

            # Initialize variables to store extracted information
            title, author, release_date, language, content = "", "", "", "", ""
            in_content = False

            for line in txt_content.splitlines():
                # Check for metadata
                title_match = title_pattern.match(line)
                if title_match:
                    title = title_match.group(1).strip()
                    continue

                author_match = author_pattern.match(line)
                if author_match:
                    author = author_match.group(1).strip()
                    continue

                release_date_match = release_date_pattern.match(line)
                if release_date_match:
                    release_date = release_date_match.group(1).strip().split('[')[0]
                    continue

                language_match = language_pattern.match(line)
                if language_match:
                    language = language_match.group(1).strip()
                    continue

                # Check for the start of content
                content_start_match = content_start_pattern.match(line)
                if content_start_match:
                    in_content = True
                    continue

                # Append lines to content if in content section
                if in_content:
                    content += line + '\n'

            content = content.strip()

            data= {
                'book_id': book_id,
                'title': title,
                'author': author,
                'release_date': release_date,
                'language': language,
                'content': content,
            }
            with open(docs_file+title+'.json', 'w', encoding='utf-8') as file:
                json.dump(data,file, indent=4)
        pass


    def initialize_scraping():
        
        for each_book in books:
            Scraping.scrape_data(each_book)
