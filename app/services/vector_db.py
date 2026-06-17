import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="business_data"
)

def save_document(doc_id, content):
    collection.add(
        documents=[content],
        ids=[doc_id]
    )

def search_documents(query):
    return collection.query(
query_texts=[query],
n_results=3
)