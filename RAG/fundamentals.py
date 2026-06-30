from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("python_notes.pdf")

documents = loader.load()

print(len(documents))

print(documents[0])

print(documents[0].page_content)

print(documents[0].metadata)