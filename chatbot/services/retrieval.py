from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from decouple import config
import os

class Retrieval:

    def __init__(self):
        pass

    def generate_answer(question,genre):

        embedding_function = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        path = os.path.join(os.path.dirname(__file__), '../models/')
        vector_db = Chroma(
            persist_directory=path+genre+"_vectordb",
            collection_name=genre,
            embedding_function=embedding_function,
        )
        # create prompt
        QA_prompt = PromptTemplate(
            template="""Use the following pieces of context to answer the user question.
        chat_history: {chat_history}
        Context: {text}
        Question: {question}
        Answer:""",
            input_variables=["text", "question", "chat_history"]
        )

        # create chat model
        llm = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"), temperature=0.6)

        # create memory
        memory = ConversationBufferMemory(
            return_messages=True, memory_key="chat_history")

        # create retriever chain
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            memory=memory,
            retriever=vector_db.as_retriever(
                search_kwargs={'fetch_k': 4, 'k': 3}, search_type='mmr'),
            chain_type="refine",
        )

        # call QA chain
        response = qa_chain({"question": question})


        return response["answer"]

        # return {"status": "success"}
        # return True