from langchain_community.chat_models import ChatOllama

def run_agent():
    llm = ChatOllama(
        model="mistral",
        temperature=0.5
    )

    user_input = input("Ask me a question: ")
    response = llm.invoke(user_input)

    print("\nAI Agent Response:\n", response.content)

if __name__ == "__main__":
    run_agent()
