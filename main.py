from dotenv import load_dotenv
load_dotenv()

from langchain_core import __version__ as core_version
from importlib.metadata import version
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI

print(f"LangChain Core version: {core_version}")
lg_version = version("langgraph")
print(f"LangGraph Version: {lg_version}")

def openai_model_check():
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    response = llm.invoke("Say 'setup complete!' in one word")
    print(response.content)

def mistral_model_check():
    llm = ChatMistralAI(model_name="mistral-small-2506", temperature=0)
    response = llm.invoke("Say 'setup complete!' in one word")
    print(response.content)

def main():
    print("Hello from productiongrade-rag!")
    openai_model_check()
    mistral_model_check()
    print("Setup complete!")


if __name__ == "__main__":
    main()
