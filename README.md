# Local AI Notes Chatbot

A simple local AI chatbot built with Python and LM Studio.

The chatbot connects to a locally running LLM through LM Studio's OpenAI-compatible server. It can answer questions, remember the conversation during the session, and use content from a notes.txt file as context.

## Features

- Runs locally using LM Studio
- No paid API required
- Terminal-based chatbot
- Maintains chat history during the session
- Answers using notes from a local text file

## Tech Stack

- Python
- LM Studio
- Local LLM
- OpenAI Python SDK

## How It Works

1. LM Studio runs a local language model.
2. Python connects to LM Studio through http://127.0.0.1:1234/v1.
3. The app loads notes.txt.
4. The chatbot answers questions using the provided notes.
5. The conversation history is stored during the session so the chatbot can understand follow-up questions.

## Run the Project

Start the LM Studio local server first.

Then run this command:

python main.py

Type your question in the terminal.

To exit the chatbot, type:

q

or:

exit

## Example Questions

What do my notes say about RAG?

Explain it in simpler words.

## Current Status

Level 1 project: local AI chatbot with memory and notes support.

## Next Improvements

- Add support for multiple notes files
- Add PDF upload support
- Add proper RAG with embeddings
- Add a simple Streamlit interface