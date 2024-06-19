from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama

llm = Ollama(model="llama3")
chat_model = ChatOllama()


from langchain_core.messages import HumanMessage

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

llm.invoke(text)
# >> Feetful of Fun

chat_model.invoke(messages)
# >> AIMessage(content="Socks O'Color")
