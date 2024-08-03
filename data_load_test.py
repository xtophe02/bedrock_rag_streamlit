import os
from langchain_community.document_loaders import PDFPlumberLoader

#2. Define the data source and load data with PDFLoader(https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf)
data_load=PDFPlumberLoader('data/expenses.pdf')
data_test=data_load.load_and_split()
print(len(data_test))
print('**'*10)
print(data_test[0].page_content)