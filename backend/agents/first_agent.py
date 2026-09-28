from langchain_ollama import ChatOllama
from langchain.tools import tool

@tool
def web_search(query: str)-> str:
    """Search the web for the given query and return a short result."""
    return f"Top result for {query}: directed graphs are used to model one-way relationships, such as despendencies, web links, and workflows."

if __name__=="__main__":
    llm= ChatOllama(model="llama3.2:3b")
    llm_with_tools= llm.bind_tools([web_search])

    response= llm_with_tools.invoke("Find out what a directed graph is used for.")
    print(response.tool_calls)