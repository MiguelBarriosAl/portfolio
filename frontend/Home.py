import sys
from pathlib import Path

import streamlit as st
from utils import ask_question

sys.path.append(str(Path(__file__).resolve().parent))


st.set_page_config(
    page_title="Miguel Barrios – AI Portfolio", page_icon="🤖", layout="wide"
)

# --- Title Row: Avatar + Intro ---
col_avatar, col_intro = st.columns([1, 3])
with col_avatar:
    st.image("frontend/assets/avatar_cyberpunk.png", width=180)

with col_intro:
    st.title("Miguel Barrios Álvarez")
    st.markdown("#### AI Engineer · MLOps · Data Engineering")
    st.markdown(
        "🚀 Welcome to my AI-powered portfolio — a dynamic space where my experience meets cutting-edge technology."
    )
    st.markdown(
        "Whether you're a recruiter or fellow engineer, feel free to explore and ask me anything!"
    )

st.divider()

# --- Ask Assistant Block ---
st.subheader("🤖 Ask me anything about my career")

query = st.text_input(
    "What do you want to know?", placeholder="e.g. What certifications do you hold?"
)
if query:
    response = ask_question(query)
    st.success(response)

st.divider()

# --- CV Download & Links ---
st.markdown("### 📄 Download CV")
cv_path = Path("data/dev/Miguel_Barrios.pdf")
if cv_path.exists():
    st.download_button(
        "Download CV",
        data=open(cv_path, "rb").read(),
        file_name="Miguel_Barrios_CV.pdf",
    )

st.markdown("### 🌐 Connect with me")
st.markdown(
    """
- [💼 LinkedIn](https://www.linkedin.com/in/miguel-barrios-alvarez)
- [🐙 GitHub](https://github.com/MiguelBarriosAl)
- [✍️ Medium](https://medium.com/@mbarriosa339)
"""
)
