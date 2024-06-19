from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
test = llm.invoke("test")

print(test)


from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def extract(user_input: str):
    entity_extraction_system_message = {"role": "system", "content": "Get me the three pricing tiers from this website's content, and return as a JSON with three keys: {cheapest: {name: str, price: float}, middle: {name: str, price: float}, most_expensive: {name: str, price: float}}"}
    
    messages = [entity_extraction_system_message]
    messages.append({"role": "user", "content": user_input})

    # Assuming llm.invoke takes a string and returns a response
    response = llm.invoke(str(messages))

    # Assuming the response from llm.invoke is similar to the response from OpenAI
    return response.choices[0].message.content



