#1. Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings import BedrockEmbeddings
from langchain_aws import BedrockLLM
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_data_and_split(file):
    #2. Define the data source and load data with 
    data_load=PDFPlumberLoader(file)
    #3. Split the Text based on Character, Tokens etc. - Recursively split by character - ["\n\n", "\n", " ", ""]
    data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=300,chunk_overlap=30)
    return [data_load,data_split]
#5c. Wrap within a function
def hr_index():
    file = 'data/expenses.pdf'
    data_load,data_split=load_data_and_split(file)
    #4. Create Embeddings -- Client connection
    data_embeddings=BedrockEmbeddings(
    credentials_profile_name= 'default',
    model_id='amazon.titan-embed-text-v1')
    #5à Create Vector DB, Store Embeddings and Index for Search - VectorstoreIndexCreator
    data_index=VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS)
    #5b  Create index for HR Policy Document
    db_index=data_index.from_loaders([data_load])
    return db_index

#6a. Write a function to connect to Bedrock Foundation Model - Claude Foundation Model
def hr_llm():
    llm=BedrockLLM(
        credentials_profile_name='default',
        model_id='anthropic.claude-v2:1',
        model_kwargs={
        "max_tokens_to_sample":3000,
        "temperature": 0.1,
        "top_p": 0.9})
    return llm
#6b. Write a function which searches the user prompt, searches the best match from Vector DB and sends both to LLM.
def hr_rag_response(index,question):
    rag_llm=hr_llm()
    hr_rag_query=index.query(question=question,llm=rag_llm)
    return hr_rag_query
# Index creation --> https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html