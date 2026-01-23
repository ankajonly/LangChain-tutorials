from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model_name="openai/gpt-oss-20b:free", temperature=0)
st.header("Research Paper Summarizer")
user_input = st.text_input("Enter the research paper text below: ")
if st.button("Summarize"):
    st.text("Summarizing the research paper...")
    result = model.invoke(user_input)
    # Add logic here to summarize the paper
    st.write(result.content)