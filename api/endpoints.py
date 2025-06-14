import shutil
from pathlib import Path

from fastapi import APIRouter, File, Header, HTTPException, UploadFile
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant
from langchain_openai import ChatOpenAI

from config import settings
from prompts.ask_profile_prompt import ASK_PROFILE_PROMPT
from schemas.ask_profile import AskRequest
from services.document_loader import load_documents
from services.vectorstore import get_vectorstore

router = APIRouter()


@router.post("/ask")
def ask_profile(input: AskRequest):
    vectorstore = get_vectorstore()
    retriever = Qdrant(
        client=vectorstore.client,
        collection_name=vectorstore.collection_name,
        embeddings=vectorstore.embedding_service.client,
    ).as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        model=settings.openai_llm_model,
        temperature=0.0,
        max_tokens=settings.max_tokens,
        request_timeout=settings.request_timeout,
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": ASK_PROFILE_PROMPT},
        return_source_documents=True,
    )

    result = qa.invoke({"query": input.query})
    return {
        "query": input.query,
        "response": result["result"],
    }


@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...), x_api_key: str = Header(None)):
    if x_api_key != settings.upload_api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

    if not (file.filename.endswith(".pdf") or file.filename.endswith(".txt")):
        raise HTTPException(
            status_code=400, detail="Only .pdf or .txt files are supported."
        )

    save_path = Path(f"data/dev/{file.filename}")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    documents = load_documents(str(save_path))
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_docs = splitter.split_documents(documents)

    texts = [doc.page_content for doc in split_docs]
    metadatas = [doc.metadata for doc in split_docs]

    store = get_vectorstore()
    store.index_documents(texts, metadatas)

    return {
        "filename": file.filename,
        "indexed_chunks": len(texts),
        "status": "success",
    }
