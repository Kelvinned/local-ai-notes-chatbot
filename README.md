# Local AI Notes Chatbot

A simple local AI chatbot built with Python and LM Studio.

The chatbot connects to a locally running LLM through LM Studio's OpenAI-compatible local server. It can answer questions in the terminal, use local notes as context, and demonstrate the basic stages of building a RAG system.

## Features

* Runs locally using LM Studio
* No paid OpenAI API required
* Terminal-based chatbot
* Maintains chat history during a session
* Uses local text notes as a knowledge source
* Includes a basic chatbot version
* Includes a manual RAG version with keyword retrieval
* Includes an embeddings-based RAG version with semantic retrieval
* Supports retrieval across multiple notes files
* Shows selected chunks and similarity scores for debugging

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

Embeddings-based RAG version using one notes file.

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

### rag_v3_multi_notes.py

Embeddings-based RAG version using multiple notes files.

It:

* reads all `.txt` files inside the `notes/` folder
* splits each file into chunks
* stores the source file name for each chunk
* converts all chunks into embeddings
* converts the user question into an embedding
* compares the question embedding with all chunk embeddings
* retrieves the most semantically similar chunks across multiple files
* shows the source file and similarity score for each selected chunk
* sends the selected chunks to the local LM Studio model

This version is closer to a real notes assistant because it can search across several files instead of relying on only one `notes.txt` file.

## How It Works

1. LM Studio runs a local language model.
2. Python connects to LM Studio through `http://127.0.0.1:1234/v1`.
3. The OpenAI Python SDK is used only as a client for LM Studio's OpenAI-compatible local API.
4. The app loads local notes as the knowledge source.
5. In `main.py`, the full `notes.txt` file is passed as context.
6. In `rag_v1.py`, relevant chunks are selected using keyword matching.
7. In `rag_v2_embeddings.py`, relevant chunks are selected using embeddings and cosine similarity.
8. In `rag_v3_multi_notes.py`, embeddings-based retrieval is performed across all text files inside the `notes/` folder.
9. The selected context is sent to the local model.
10. The model answers using the provided notes.

## Important Note

This project does not send requests to OpenAI's paid servers.

The OpenAI Python SDK is used because LM Studio provides an OpenAI-compatible local API. The requests are sent to the local LM Studio server running on the user's own computer.

## Project Structure

```text
local-ai-notes-chatbot/
├── main.py
├── rag_v1.py
├── rag_v2_embeddings.py
├── rag_v3_multi_notes.py
├── notes.txt
├── notes/
│   ├── ai_basics.txt
│   └── python_basics.txt
├── README.md
├── requirements.txt
└── .gitignore
```

## Run the Project

Start the LM Studio local server first.

To run the basic chatbot:

```bash
python main.py
```

To run the manual keyword-based RAG version:

```bash
python rag_v1.py
```

To run the embeddings-based RAG version using one notes file:

```bash
python rag_v2_embeddings.py
```

To run the embeddings-based RAG version using multiple notes files:

```bash
python rag_v3_multi_notes.py
```

To exit any chatbot, type:

```text
q
```

or:

```text
quit
```

or:

```text
exit
```

## Example Questions

What do my notes say about RAG?

What is LM Studio?

What are embeddings?

What is a Python function?

What is the difference between local LLM and API in this project?

What is the difference between outside files and model memory?

## Current Status

The project currently has:

* local chatbot connected to LM Studio
* session memory in the basic chatbot
* notes-based context support
* manual RAG-style retrieval using keyword matching
* embeddings-based retrieval using SentenceTransformers
* cosine similarity search using scikit-learn
* retrieval across multiple `.txt` notes files
* source file display for retrieved chunks
* similarity score display for retrieved chunks
* low-confidence warning for weak retrieval results
* GitHub repository setup

## Limitations

* The chatbot currently supports only text files
* PDF support is not added yet
* Memory is session-based and not stored permanently
* The embeddings version is simple and does not use a vector database
* Embeddings are recalculated each time the script starts
* The local model is small, so answer quality may be limited
* Retrieval quality depends heavily on good notes and good chunking

## What I Learned

This project demonstrates:

* how to connect Python to a local LLM
* how LM Studio can expose a local OpenAI-compatible API
* how chat memory can be stored during a session
* how external notes can be passed as context
* how basic RAG works
* the difference between keyword retrieval and embeddings-based retrieval
* how cosine similarity can be used to compare question and chunk embeddings
* why retrieval confidence matters in RAG systems
* why good notes and chunking affect answer quality

## Next Improvements

* Add PDF support
* Add a simple Streamlit interface
* Add persistent chat history
* Store embeddings in a vector database
* Avoid recalculating embeddings every run
* Later experiment with LangChain
