from langchain_openai import ChatOpenAI
from dotenv import load_dotenv    

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    temperature=0.7
)

response = llm.invoke("Kudhila kise kehte hai")
print(response.content)
