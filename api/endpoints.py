from fastapi import APIRouter
from langchain.chains import RetrievalQA
from langchain.vectorstores.qdrant import Qdrant
from langchain_community.llms import Ollama
from pydantic import BaseModel

from services.vectorstore import get_vectorstore

router = APIRouter()


class QueryInput(BaseModel):
    query: str


@router.post("/ask")
def ask_profile(input: QueryInput):
    vectorstore = get_vectorstore()

    # Creamos el retriever de langchain sobre Qdrant
    retriever = Qdrant(
        client=vectorstore.client,
        collection_name=vectorstore.collection_name,
        embeddings=vectorstore.embedding_service.client,
    ).as_retriever()

    # Carga del modelo local (ajústalo si usas otro modelo)
    llm = Ollama(model="mistral")

    # Chain de respuesta con recuperación
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,  # Opcional si quieres incluir chunks
    )

    result = qa.invoke({"query": input.query})
    return {"query": input.query, "response": result["result"]}
