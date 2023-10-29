from langchain.document_loaders import JSONLoader,TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# med_loader = JSONLoader(
#     jq_schema='.[]',
#     file_path='qna/qna_train_webmd_squad_v2_full.json',
#     text_content=False
# )

med_loader=TextLoader('sentences_train_webmd_squad_v2_full.txt')

med_data = med_loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
all_splits = text_splitter.split_documents(med_data)

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cuda'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

vectorstore = Chroma.from_documents(documents=all_splits, embedding=hf, persist_directory='./chroma_db_train')
vectorstore.persist()

question = 'What are some tips to handle bipolar disorder?'
docs = vectorstore.similarity_search(question)
print(len(docs))
print(docs)
