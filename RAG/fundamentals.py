from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
# passes the user's input forward unchanged
from langchain_core.runnables import RunnablePassthrough
#
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# this will get google ai embedding model
# an embedding model is used to convert any data,image into numbers
# which is called a vector and can be stored in a vector database
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

loader = PyPDFLoader(r"C:\Users\HP\OneDrive\Documents\ai automation python\RAG\test.pdf")

documents = loader.load()

# print(len(documents))

# print(documents[0])

# print(documents[0].page_content)

# print(documents[0].metadata)

# Creates the text splitter
splitter = RecursiveCharacterTextSplitter(
    # each chunk should have a 1000 characters not words
    chunk_size=1000,

    # each chunk should have the last 200 char from the previous chunk
    # this preserve context
    chunk_overlap=200
)

# Creates chunk of each page one by one and store in 
# the chunks variable
chunks = splitter.split_documents(documents)

# print(len(chunks))

# for i in range (1,4):
#     print(len(chunks))
#     print(chunks[i].page_content)
#     print(chunks[i].metadata)

# creates a vector database
# FAISS automatically loops through every chunk creates the embedding
# through the ai model and save them in vector database
# vector_db = FAISS.from_documents(
#     documents=chunks,
#     embedding=embeddings
# )

# vector_db.save_local("faiss_db")

vector_db = FAISS.load_local(
    "faiss_db",
    embeddings,
    allow_dangerous_deserialization=True
)
# after this line finishes
# PDF

# ↓

# Chunks

# ↓

# Vectors

# ↓

# FAISS

# results = vector_db.similarity_search(
#     "What is Python?",
    # meaning return top 3 most similar chunks
#     k=3
# )

# to acess the first chunk text
# print(results[0].page_content)

# for i, doc in enumerate(results, start=0):
#     print("=" * 50)
#     print(f"Result {i}")
#     print("=" * 50)
#     print(doc.page_content)
#     print()
#     print(doc.metadata)
#     print()


# Using retriever bcz LangChain recommends it
retriever = vector_db.as_retriever(
    # Always retrieve the 3 closest chunks.
    search_kwargs={"k":3}
)

question = input("Ask a Question: ")

prompt = ChatPromptTemplate.from_template("""
Answer the following question using ONLY the provided context.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I don't know."

Answer:
""")

rag_chain = (
    {
        "context" : retriever,
        "question" : RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

result = rag_chain.invoke(question)

# docs = retriever.invoke(question)

print(result)
# for i, doc in enumerate(docs, start=1):
    # print("\n" + "=" * 60)
    # print("ANSWER")
    # print("=" * 60)
    # print(result)
    # print("="*50)
    # print(f"Source {i}")
    # print(doc.metadata)
    # print(doc.page_content)
