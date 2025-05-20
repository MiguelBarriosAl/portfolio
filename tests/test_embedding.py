from services.embedding import EmbeddingService


def test_embed_query_returns_vector():
    service = EmbeddingService()
    query = "What is your experience with Python?"
    vector = service.embed_query(query)

    assert isinstance(vector, list)
    assert all(isinstance(v, float) for v in vector)
    assert len(vector) > 10
