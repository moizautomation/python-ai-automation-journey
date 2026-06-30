from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("test.pdf")

documents = loader.load()

# print(len(documents))

# print(documents[0])

# print(documents[0].page_content)

# print(documents[0].metadata)

# Creates the text splitter
splitter = RecursiveCharacterTextSplitter(
    # each chunk should have a 1000 characters not words
    chunk_size=1000,

    # each chunk should have the last 200 char from the previous chuunk
    # this preserve context
    chunk_overlap=200
)

# Creates chunk of each page one by one and store in 
# the chunks variable
chunks = splitter.split_documents(documents)

# print(len(chunks))

for i in range (1,4):
    print(len(chunks))
    print(chunks[i].page_content)
    print(chunks[i].metadata)

