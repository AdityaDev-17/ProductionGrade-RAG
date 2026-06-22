import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import (TextLoader, WebBaseLoader, DirectoryLoader,PyPDFLoader)

from dotenv import load_dotenv
load_dotenv()

def load_text_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name
    
    try:
        loader = TextLoader(temp_file_path)
        documents = loader.load()
        print(f"Loaded {len(documents)} document(s)")
        print(f"Content preview: {documents[0].page_content[:100]}...")
        print(f"Metadata: {documents[0].metadata}")

        for doc in documents:
            print(f"Document content: {doc.page_content}")
            print(f"Document metadata: {doc.metadata}")

    finally:
        os.remove(temp_file_path)

def load_pdf_file(pdf_path : str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} document(s) from PDF")

    for i, doc in enumerate(documents):
        print(f"Document {i + 1} content: {doc.page_content[:100]}...")
        print(f"Document {i + 1} metadata: {doc.metadata}")

if __name__ == "__main__":
    #load_text_file()  
    load_pdf_file("U:\AI\AIProjects\ProductionGrade-RAG\docs\deeplearning.pdf") 
