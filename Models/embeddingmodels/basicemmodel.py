from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
documents = [
    "LangChain is used to build LLM applications",
    "Embeddings convert text into vectors",
    "Vector databases help in semantic search"
    # \evelopers to build robust and scalable applications that leverage the capabilities of large language models
]

embedding_model = OpenAIEmbeddings(
    model = "openai/text-embedding-3-small"

)
embeddings = embedding_model.embed_documents(documents)

for doc, emb in zip(documents, embeddings):
    print(f"Document: {doc}\nEmbedding: {emb}\n")
