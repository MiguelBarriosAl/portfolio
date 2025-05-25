import requests

from config import API_URL


def ask_question(query: str) -> str:
    try:
        res = requests.post(f"{API_URL}/ask", json={"query": query})
        res.raise_for_status()
        return res.json().get("response", "No response found.")
    except requests.RequestException as e:
        return f"Request failed: {e}"
    except ValueError:
        return f"Invalid JSON response: {res.text}"


def upload_file(file) -> bool:
    files = {"file": (file.name, file.getvalue())}
    res = requests.post(f"{API_URL}/upload-file", files=files)
    return res.status_code == 200
