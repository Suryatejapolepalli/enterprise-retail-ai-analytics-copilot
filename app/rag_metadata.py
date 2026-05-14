import faiss
import numpy as np

from openai import OpenAI
from metadata_documents import metadata_docs

client = OpenAI()

documents = [
    doc["content"]
    for doc in metadata_docs
]

# ============================================
# CREATE EMBEDDINGS
# ============================================

embeddings = []

for doc in documents:

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=doc
    )

    embeddings.append(
        response.data[0].embedding
    )

embedding_array = np.array(
    embeddings,
    dtype="float32"
)

# ============================================
# FAISS INDEX
# ============================================

index = faiss.IndexFlatL2(
    embedding_array.shape[1]
)

index.add(embedding_array)

# ============================================
# SEARCH FUNCTION
# ============================================

def search_metadata(query):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    query_embedding = np.array(
        [response.data[0].embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        1
    )

    return documents[
        indices[0][0]
    ]