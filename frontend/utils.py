import requests

from config import API_BASE_URL


def ask_question(query: str) -> str:
    try:
        res = requests.post(f"{API_BASE_URL}/ask", json={"query": query})
        res.raise_for_status()
        return res.json().get("response", "No response found.")
    except requests.RequestException as e:
        return f"Request failed: {e}"
    except ValueError:
        return f"Invalid JSON response: {res.text}"
