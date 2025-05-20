from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain_core.runnables import Runnable

from services.vectorstore import get_vectorstore

store = get_vectorstore()


def get_query_engine() -> Runnable:
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()
    llm = Ollama(model="llama3")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa


def query_user_profile(query: str) -> str:
    engine = get_query_engine()
    result = engine.run(query)
    return result
