from langchain.agents import create_agent
from langchain_ollama.chat_models import ChatOllama
from langchain.tools import tool
from typing import Dict, Any
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for information"""
    return search.invoke(query)

system_prompt = """
You are a personal chef. The user will give you a list of ingredients they have left over in their house.
Using the web search tool, search the web for recipes that can be made with the ingredients they have.
Return recipe suggestions and eventually the recipe instructions to the user, if requested.
"""


model = ChatOllama(model="qwen3.5")

agent = create_agent(
    model = model, system_prompt=system_prompt, tool=[web_search]
)