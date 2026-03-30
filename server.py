from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

app = Flask(__name__)
CORS(app)

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
    global chat_history
    current_turns = len(chat_history) // 2
    if current_turns >= MAX_TURNS:
        return {
            "response": "Context window is full\nThe AI not follow your previous thread properly\nPlease click 'New Chat' for a new chat",
            "remaining": 0,
            "context_full": True
        }

    response = chain.invoke({
        "question": question,
        "chat_history": chat_history
    })
    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=response))

    remaining = MAX_TURNS - (current_turns + 1)
    return {"response": response, "remaining": remaining}

@app.route('/')
def index():
    model_info = {
        "model": "minimax-m2.5:cloud",
        "temperature": 0.7
    }
    return render_template('index.html', model_info=model_info)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json()
    question = data.get('message', '')

    if question.lower() == 'clear':
        chat_history.clear()
        return jsonify({"response": "Chat history cleared.", "remaining": MAX_TURNS})

    result = chat(question)
    return jsonify(result)

@app.route('/api/clear', methods=['POST'])
def api_clear():
    chat_history.clear()
    return jsonify({"response": "Chat history cleared.", "remaining": MAX_TURNS})

if __name__ == "__main__":
    app.run(debug=True, port=5000)