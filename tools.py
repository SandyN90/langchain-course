from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
import os

@tool
def search(query: str) -> str:
    """Search the web for information
    Args:
        query: The query to search for
    """
    print(f'Searching the web for information about {query}')
    return "the capital of France is Parish"

tools = [search]
# model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", api_key=os.getenv("GEMINI_API_KEY"))
model = ChatOllama(temperature=0, model="gemma4:e2b")
agent = create_agent(model=model, tools=tools)
# response = agent.invoke({"messages": HumanMessage(content=query)})
    