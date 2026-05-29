from openai import OpenAI
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_notes():
    with open("notes.txt", "r") as file:
        return file.read()


def split_into_chunks(text):
    return text.split("\n\n")


def find_relevant_chunks(question, chunks, chunk_embeddings):
    question_embedding = embedding_model.encode([question])

    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]

    ranked_chunks = sorted(
        zip(similarities, chunks),
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked_chunks[:5] # Return top 5 relevant chunks


notes = load_notes()
chunks = split_into_chunks(notes)
chunk_embeddings = embedding_model.encode(chunks)

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
        print(f"- Score: {score:.2f}")
        print(chunk)

    context = "\n\n".join([chunk for score, chunk in relevant_chunks])

    response = client.chat.completions.create(
        model="llama-3.2-3b-instruct",
        messages=[
            {
                "role": "system",
                "content": f"""
You are a strict notes assistant.

Use ONLY the context below.
Do not add outside knowledge.
Answer directly from the context. Do not say "based on inference" if the context contains the answer.
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