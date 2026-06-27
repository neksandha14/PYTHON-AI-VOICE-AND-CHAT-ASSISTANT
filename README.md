# Python AI Voice and Chat Assistant

## Overview

Python AI Voice and Chat Assistant is a command-line application that provides basic conversational capabilities through text and voice responses. The assistant can greet users, answer simple questions, provide the current time, and perform mathematical calculations using voice output powered by a text-to-speech engine.

This project demonstrates the fundamentals of building a simple AI assistant using Python.

---

## Features

* Interactive text-based chat interface
* Voice responses using Text-to-Speech (TTS)
* Greeting and conversation support
* Current time retrieval
* Basic calculator functionality
* Continuous conversation until the user exits
* Beginner-friendly implementation

---

## Technologies Used

* Python 3
* pyttsx3
* datetime

---

## Project Structure

```text
Python-AI-Voice-Chat-Assistant/
│
├── ai_assistant.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Python-AI-Voice-Chat-Assistant.git
```

Navigate to the project directory:

```bash
cd Python-AI-Voice-Chat-Assistant
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## Requirements

* Python 3.9 or later
* pyttsx3

Install manually if needed:

```bash
pip install pyttsx3
```

---

## Run the Application

```bash
python ai_assistant.py
```

or

```bash
python3 ai_assistant.py
```

---

## Example Interaction

```text
Oliver: Hello! I am your AI Assistant.
Type "exit" to end the conversation.

You: hello

AI Bot:
Hello! How can I assist you today?

You: what is your name

AI Bot:
I am Oliver, your AI Assistant. How can I help you today?

You: time

AI Bot:
The current time is 18:45:12

You: calculate 25 * 4

AI Bot:
The result is 100
```

---

## Supported Commands

* hello
* hi
* how are you
* what is your name
* time
* calculate <expression>
* exit

---

## Learning Objectives

This project demonstrates:

* Python functions
* Conditional statements
* Loops
* User input handling
* Text-to-Speech using pyttsx3
* Working with date and time
* Basic expression evaluation
* Building a simple conversational assistant

---

## Future Improvements

* Voice input using SpeechRecognition
* Weather information
* Open websites using voice commands
* Play music
* Wikipedia search
* AI-powered responses using Large Language Models (LLMs)
* Reminder and alarm functionality
* File management commands
* Email automation
* Graphical User Interface (GUI)
* Integration with OpenAI or Ollama models

---

## Security Note

The current calculator feature uses Python's `eval()` function for evaluating mathematical expressions. For production applications, it is recommended to replace `eval()` with a safer expression parser to prevent the execution of arbitrary code.

---

## Author

**Nek Sandha**

B.Tech Computer Science Engineering

Python | Artificial Intelligence | Generative AI | Automation | Machine Learning
