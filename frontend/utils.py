import requests

from config import API_URL


def ask_question(query: str) -> str:
    res = requests.post(f"{API_URL}/ask", json={"query": query})
    return res.json()["response"]


def upload_file(file) -> bool:
    files = {"file": (file.name, file.getvalue())}
    res = requests.post(f"{API_URL}/upload-file", files=files)
    return res.status_code == 200
