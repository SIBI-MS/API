import streamlit as st
from main import get_pdf_data,get_pdf_chunks


st.set_page_config("API")
st.title("API")

tab1,tab2,tab3=st.tabs(['PDF',"WebLink","Others"])


with tab1:
    pdf_data=st.file_uploader("Upload the document...",accept_multiple_files=True)
    if st.button("Process"):
        with st.spinner("Loading..."):
            
            #Extract data from the pdfs
            pdf_document=get_pdf_data(pdf_data)
            
            #To get chunks from the pdf data
            pdf_chunks=get_pdf_chunks(pdf_document)
            
            #To create and store embeddings
            pdf_vector_store=get_pdf_vector_store(pdf_chunks)
            
            
            
with tab2:
    pass

with tab3:
    pass
    