import streamlit as st
import os
import pickle
import time
from langchain.llms import HuggingFaceEndpoint
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
st.title("URL Information Extractor")
st.sidebar.title("Webpage Urls")
urls=[]
llm = HuggingFaceEndpoint(repo_id='deepseek-ai/DeepSeek-R1', task='text-generation', temperature=0.3)
filepath='faiss_store.pkl'
main_placeholder=st.empty()

with st.sidebar:
    for i in range(3):
        url=st.text_input(f"URL {i+1}")
        urls.append(url)
    processed_url_clicked=st.button("Process Url")

if(processed_url_clicked):
    loader=UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Loading Data... ✅✅✅")
    data=loader.load()
    textsplit=RecursiveCharacterTextSplitter(separators=['\n\n','\n','.',','],chunk_size=1000,chunk_overlap=200)
    docs=textsplit.split_documents(data)
    main_placeholder.text("Splitting into Chunks... ✅✅✅")
    embedding=HuggingFaceEmbeddings(model_name='all-mpnet-base-v2')
    vector_db=FAISS.from_documents(docs,embedding)
    main_placeholder.text("Creating Vector Database... ✅✅✅")
    with open(filepath,"wb") as f:
        pickle.dump(vector_db,f)

query=main_placeholder.text_input("Enter Your Query")
if(query):
    if(os.path.exists(filepath)):
        with open(filepath,'rb') as f:
            vector_store=pickle.load(f)
            chain=RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever=vector_store.as_retriever())
            result=chain({'question':query},return_only_outputs=True)
            st.header("Answer")
            st.write(result['answer'])
            sources=result.get("sources","")
            if(sources):
                st.subheader("Sources:")
                source_list=set(sources.split(","))
                for source in source_list:
                    st.write(source)
