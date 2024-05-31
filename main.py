import fitz 
from langchain_text_splitters import RecursiveCharacterTextSplitter


#Extract data from the pdfs
def get_pdf_data(pdf_data):
  text = ""
  for pdf in pdf_data:
    with fitz.open(pdf) as doc:
      text += doc.extract_text()
  return text


#To get chunks from the pdf data
def get_pdf_chunks(pdf_document):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    pdf_chunks=text_splitter.split_text(pdf_document)
    return pdf_chunks


#To create and store embeddings
def get_pdf_vector_store(pdf_chunks):
    embeddings=

def main():
    pass

if __name__=="__main__":
    main()
    