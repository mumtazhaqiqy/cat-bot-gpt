import streamlit as st

st.title('Hello in Project')

def read_file(file):
    file_content = file.read()
    st.write(file_content)

uploaded_file = st.file_uploader("Choose a file", type="txt")

if uploaded_file is not None:
    read_file(uploaded_file)
    