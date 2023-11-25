from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import os
import re


class DataLoading:

    def __init__(self):
        pass
    
    def to_snake_case(input_string):
        alpha_only = re.sub(r'[^a-zA-Z ]', '', input_string)
        alpha_only = alpha_only.replace(' ', '_')
        snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', alpha_only).lower()
        return snake_case


    def load_data():
        folder_path = os.path.join(os.path.dirname(__file__), '../../documents/')
        files = os.listdir(folder_path)
        for file in files:
            file_name = file[:-4]
            file_name = DataLoading.to_snake_case(file_name)
            loader = PyPDFLoader(folder_path+file)
            pages = loader.load_and_split()
            embedding_function = SentenceTransformerEmbeddings(
                model_name='all-MiniLM-L6-v2'
            )
            vectordb = Chroma.from_documents(
                documents=pages,
                embedding=embedding_function,
                persist_directory="../models/"+file_name+"_vectordb",
                collection_name=file_name
            )
            vectordb.persist()
        pass
        
                
DataLoading.load_data()
