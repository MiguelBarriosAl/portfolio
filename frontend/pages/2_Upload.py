import streamlit as st

from frontend.utils import upload_file

st.title("Upload your CV (PDF or TXT)")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt"])

if uploaded_file and st.button("Upload"):
    success = upload_file(uploaded_file)
    if success:
        st.success("File uploaded and indexed!")
    else:
        st.error("Upload failed.")
