from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)
client.upsert(
    collection_name="docs",
    points=[
        {"id": 1, "vector": embeddings, "payload": {"text": "Python asyncio tutorial"}}
    ],
)

results = client.search(collection_name="docs", query_vector=query_embedding, limit=5)
