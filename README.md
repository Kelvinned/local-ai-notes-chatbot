# Local AI Notes Chatbot

A simple local AI chatbot built with Python and LM Studio.

The chatbot connects to a locally running LLM through LM Studio's OpenAI-compatible local server. It can answer questions in the terminal, use a local notes file as context, and demonstrate basic RAG concepts.

## Features

* Runs locally using LM Studio
* No paid OpenAI API required
* Terminal-based chatbot
* Maintains chat history during a session
* Uses `notes.txt` as a local knowledge source
* Includes a basic chatbot version
* Includes a manual RAG version with keyword retrieval
* Includes an embeddings-based RAG version with semantic retrieval

## Tech Stack

* Python
* LM Studio
* Local LLM
* OpenAI Python SDK
* SentenceTransformers
* scikit-learn
* Git and GitHub

## Project Versions

### main.py

Basic local chatbot connected to LM Studio.

It supports:

* terminal chat
* session memory
* loading `notes.txt` as context
* sending the full notes file to the local model

This version is useful for understanding how Python connects to a local LLM through LM Studio.

### rag_v1.py

Manual RAG-style version using keyword retrieval.

It:

* reads `notes.txt`
* splits the notes into chunks
* retrieves relevant chunks using keyword matching
* sends only the selected chunks to the local model
* answers based on the retrieved context

This version does not use embeddings or LangChain. It was built manually to understand the basic retrieval process before using more advanced tools.

### rag_v2_embeddings.py

Embeddings-based RAG version.

It:

* reads `notes.txt`
* splits the notes into chunks
* converts note chunks into embeddings using SentenceTransformers
* converts the user question into an embedding
* compares the question embedding with chunk embeddings using cosine similarity
* retrieves the most semantically similar chunks
* sends the selected chunks to the local LM Studio model
* shows similarity scores for retrieved chunks
* gives a warning when retrieval confidence is low

This version improves over keyword search because it retrieves chunks by meaning, not only exact word matches.

## How It Works

1. LM Studio runs a local language model.
2. Python connects to LM Studio through `http://127.0.0.1:1234/v1`.
3. The OpenAI Python SDK is used only as a client for LM Studio's OpenAI-compatible local API.
4. The app loads `notes.txt` as the knowledge source.
5. In `main.py`, the full notes file is passed as context.
6. In `rag_v1.py`, relevant chunks are selected using keyword matching.
7. In `rag_v2_embeddings.py`, relevant chunks are selected using embeddings and cosine similarity.
8. The selected context is sent to the local model.
9. The model answers using the provided notes.

## Important Note

This project does not send requests to OpenAI's paid servers.

The OpenAI Python SDK is used because LM Studio provides an OpenAI-compatible local API. The requests are sent to the local LM Studio server running on the user's own computer.

## Run the Project

Start the LM Studio local server first.

To run the basic chatbot:

python main.py

To run the manual keyword-based RAG version:

python rag_v1.py

To run the embeddings-based RAG version:

python rag_v2_embeddings.py

To exit any chatbot, type:

q, quit or exit

## Example Questions

What do my notes say about RAG?

What is LM Studio?

What are embeddings?

What is the difference between local LLM and API in this project?

What is the difference between outside files and model memory?

## Current Status

The project currently has:

* local chatbot connected to LM Studio
* session memory in the basic chatbot
* notes-based context support
* manual RAG-style retrieval using keyword matching
* embeddings-based retrieval using SentenceTransformers
* similarity score display for retrieved chunks
* low-confidence warning for weak retrieval results
* GitHub repository setup

## Limitations

* The chatbot currently uses only `notes.txt`
* PDF support is not added yet
* Memory is session-based and not stored permanently
* The embeddings version is simple and does not use a vector database
* The local model is small, so answer quality may be limited
* Retrieval quality depends heavily on good notes and good chunking

## Next Improvements

* Add support for multiple notes files
* Add PDF support
* Add a simple Streamlit interface
* Add persistent chat history
* Store embeddings in a vector database
* Later experiment with LangChain
