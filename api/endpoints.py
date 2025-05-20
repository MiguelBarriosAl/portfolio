from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class QueryInput(BaseModel):
    query: str


@router.post("/ask")
def ask_profile(input: QueryInput):
    # Lógica que consulta al vectorstore + LLM
    return {"response": f"Pregunta recibida: {input.query}"}
