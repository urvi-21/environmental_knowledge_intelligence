import faiss
import numpy as np

from embedder import model

from utils import (
    environmental_score,
    scientific_density_score
)


class VectorStore:

    def __init__(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.array(embeddings).astype("float32")
        )

    def search(self, query_embedding, top_k=10):

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k
        )

        return indices[0]


def retrieve_chunks(query, vector_store, chunks, top_k=3):

    # ----------------------------------------
    # CREATE QUERY EMBEDDING
    # ----------------------------------------

    query_embedding = model.encode([query])[0]

    # ----------------------------------------
    # RETRIEVE INITIAL SEMANTIC MATCHES
    # ----------------------------------------

    indices = vector_store.search(
        query_embedding,
        top_k=10
    )

    scored_chunks = []

    # ----------------------------------------
    # RE-RANK CHUNKS
    # ----------------------------------------

    for rank_position, idx in enumerate(indices):

        chunk = chunks[idx]

        # ----------------------------------------
        # ENVIRONMENTAL SCORE
        # ----------------------------------------

        env_score = environmental_score(chunk)

        # ----------------------------------------
        # SCIENTIFIC DENSITY SCORE
        # ----------------------------------------

        sci_score = scientific_density_score(chunk)

        # ----------------------------------------
        # SEMANTIC SCORE
        # Higher-ranked chunks receive
        # higher semantic importance
        # ----------------------------------------

        semantic_score = 10 - rank_position

        # ----------------------------------------
        # FINAL IMPORTANCE SCORE
        # ----------------------------------------

        final_score = (
            semantic_score * 0.5
            + env_score * 0.3
            + sci_score * 0.2
        )

        scored_chunks.append(
            (
                chunk,
                final_score,
                env_score,
                sci_score,
                semantic_score
            )
        )

    # ----------------------------------------
    # SORT BY FINAL SCORE
    # ----------------------------------------

    scored_chunks = sorted(
        scored_chunks,
        key=lambda x: x[1],
        reverse=True
    )

    # ----------------------------------------
    # RETURN TOP CHUNKS
    # ----------------------------------------

    top_chunks = scored_chunks[:top_k]

    return top_chunks