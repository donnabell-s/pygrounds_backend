# vector_db/chroma_utils.py
from adminpanel.models import DocumentChunk
from vector_db.chroma_manager import embedding_model, collection

def store_chunks_to_chroma(document, toc_entry, chunks):
    for i, chunk in enumerate(chunks):
        text = chunk['content'] if isinstance(chunk, dict) else chunk

        # Optional Django save
        DocumentChunk.objects.create(
            document=document,
            toc_entry=toc_entry,
            chunk_order=i,
            content=text
        )

        # Save to vector DB
        embedding = embedding_model.encode(text).tolist()
        collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[f"{document.id}-{toc_entry.id}-{i}"],
            metadatas=[{
                "document_id": document.id,
                "toc_title": toc_entry.title,
                "chunk_order": i
            }]
        )
