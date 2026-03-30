# AI Chatbot

A stunning AI chatbot with a beautiful dark UI powered by LangChain and Ollama.

## Features

- Sleek cosmic dark theme with glowing accents
- Animated message bubbles with smooth transitions
- Glassmorphism effects
- Typing indicator animation
- Responsive design
- Sidebar showing model name and temperature settings
- New Chat button to start fresh conversations
- Context full message when 5 turns limit is reached

## Requirements

- Python 3.10+
- Ollama installed with `minimax-m2.5:cloud` model

## Installation

1. Install dependencies:
```bash
pip install flask flask-cors langchain langchain-ollama
```

2. Make sure Ollama is running with the model:
```bash
ollama run minimax-m2.5:cloud
```

## Running the Chatbot

```bash
python server.py
```

Then open your browser to: **http://localhost:5000**

## Files

- `server.py` - Flask backend server
- `templates/index.html` - Frontend UI
- `static/favicon.svg` - Favicon
- `main.py` - Original CLI chatbot