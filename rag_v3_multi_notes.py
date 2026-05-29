from openai import OpenAI
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_notes_from_folder(folder_path):
    all_notes = []

    for file_path in Path(folder_path).glob("*.txt"):
        with open(file_path, "r") as file:
            text = file.read()
            all_notes.append((file_path.name, text))

    return all_notes


def split_into_chunks(all_notes):
    chunks = []

    for file_name, text in all_notes:
        sections = text.split("\n\n")

        for section in sections:
            if section.strip():
                chunks.append({
                    "source": file_name,
                    "text": section
                })

    return chunks


def find_relevant_chunks(question, chunks, chunk_embeddings):
    question_embedding = embedding_model.encode([question])

    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]

    ranked_chunks = sorted(
        zip(similarities, chunks),
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked_chunks[:5]


all_notes = load_notes_from_folder("notes")
chunks = split_into_chunks(all_notes)
chunk_texts = [chunk["text"] for chunk in chunks]
chunk_embeddings = embedding_model.encode(chunk_texts)

while True:
    user_question = input("\nAsk something: ")

    if user_question.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break

    relevant_chunks = find_relevant_chunks(user_question, chunks, chunk_embeddings)

    best_score = relevant_chunks[0][0]

    if best_score < 0.35:
        print("\nWarning: Low retrieval confidence. The answer may be weak.")

    print("\nSelected chunks:")
    for score, chunk in relevant_chunks:
        print(f"- Source: {chunk['source']} | Score: {score:.2f}")
        print(chunk["text"])

    context = "\n\n".join(
        [f"Source: {chunk['source']}\n{chunk['text']}" for score, chunk in relevant_chunks]
    )

    response = client.chat.completions.create(
        model="llama-3.2-3b-instruct",
        messages=[
            {
                "role": "system",
                "content": f"""
You are a strict notes assistant.

Use ONLY the context below.
Answer directly from the context.
If the answer is not in the context, say: "The topic isn't discussed in the notes."

Context:
{context}
"""
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
        temperature=0.1
    )

    print("\nAI:", response.choices[0].message.content)