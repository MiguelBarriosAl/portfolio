import streamlit as st

from frontend.utils import ask_question

st.title("💬 Ask me about my experience")

query = st.text_input("Type your question here")

if st.button("Ask") and query:
    response = ask_question(query)
    st.success(f"**Answer:** {response}")
