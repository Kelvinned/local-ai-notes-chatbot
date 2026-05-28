# Local AI Notes Chatbot

A simple local AI chatbot built with Python and LM Studio.

The chatbot connects to a locally running LLM through LM Studio's OpenAI-compatible server. It can answer questions, remember the conversation during the session, and use content from a `notes.txt` file as context.

## Features

- Runs locally using LM Studio
- No paid API required
- Terminal-based chatbot
- Maintains chat history during the session
- Answers using notes from a local text file
- Includes a manual RAG-style version with keyword retrieval

## Tech Stack

- Python
- LM Studio
- Local LLM
- OpenAI Python SDK
- Git and GitHub

## Project Versions

### main.py

Basic local chatbot connected to LM Studio.

It supports:
- terminal chat
- session memory
- loading `notes.txt` as context

### rag_v1.py

Manual RAG-style version.

It:
- reads `notes.txt`
- splits the notes into chunks
- retrieves relevant chunks using keyword matching
- sends only the selected chunks to the local model
- answers based on the retrieved context

This version does not use embeddings or LangChain yet. It is built manually to understand how retrieval works before using advanced tools.

## How It Works

1. LM Studio runs a local language model.
2. Python connects to LM Studio through `http://127.0.0.1:1234/v1`.
3. The app loads `notes.txt`.
4. In `main.py`, the full notes file is passed as context.
5. In `rag_v1.py`, only relevant chunks are selected and passed as context.
6. The model answers using the provided notes.

## Run the Project

Start the LM Studio local server first.

To run the basic chatbot:

python main.py

To run the manual RAG version:

python rag_v1.py

To exit the chatbot, type q or exit


## Example Questions

What do my notes say about RAG?

What is LM Studio?

What are embeddings?

What is the difference between local LLM and API in this project?

## Current Status

The project currently has:

- local chatbot with memory
- notes-based context support
- manual RAG-style retrieval using keyword matching
- GitHub repository setup

## Next Improvements

- Improve retrieval with embeddings
- Add support for multiple notes files
- Add PDF support
- Add a simple Streamlit interface
- Later experiment with LangChain