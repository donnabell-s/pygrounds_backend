# vector_db/chroma_manager.py
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Setup once here
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

collection = client.get_or_create_collection(name="document_chunks")
