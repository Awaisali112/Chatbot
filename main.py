from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="minimax-m2.5:cloud",
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages(
    [
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}"),
    ]
)
chain = prompt | llm | StrOutputParser()

chat_history = []
MAX_TURNS = 5

def chat(question):
    current_turns = len(chat_history) // 2
    if current_turns >= MAX_TURNS:
        return(
            "Context windows is full"
            "The AI not follow your previous thread properly"
            "PLease type 'clear' for a new chat"
        )


    response = chain.invoke({
        "question": question,
        "chat_history": chat_history
    })
    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=response))

    remaining = MAX_TURNS - (current_turns + 1)
    if remaining <= 2:
        response += f"your{remaining} turns left"

    return response


def main():
    print("Langchain Chatbot ready! (Type 'exit' to quit, 'clear' to start a new chat)")
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "exit":
            break
        if user_input.lower() == "clear":
            chat_history.clear()
            print("Chat history cleared.")
        chat_response = chat(user_input)
        print(f"AI: {chat_response}")


if __name__ == "__main__":
    main()


                        