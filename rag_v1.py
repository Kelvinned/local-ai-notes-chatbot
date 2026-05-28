from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def load_notes():
    with open("notes.txt", "r") as file:
        return file.read()

def split_into_chunks(text):
    return text.split(". ")

def find_relevant_chunks(question, chunks):
    question_words = question.lower().split()
    relevant_chunks = []

    for chunk in chunks:
        chunk_lower = chunk.lower()

        for word in question_words:
            if word in chunk_lower:
                relevant_chunks.append(chunk)
                break

    return relevant_chunks[:3]

notes = load_notes()
chunks = split_into_chunks(notes)

while True:
    user_question = input("\nAsk something: ")

    if user_question.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break

    relevant_chunks = find_relevant_chunks(user_question, chunks)
    if not relevant_chunks:
        print("\nAI: The topic isn't discussed in the notes.")
        continue
    print("\nSelected chunks:")
    for chunk in relevant_chunks:
        print("-", chunk)
    
    context = "\n".join(relevant_chunks)

    response = client.chat.completions.create(
        model="llama-3.2-3b-instruct",
        messages=[
            {
                "role": "system",
                "content": f"""
                You are a strict notes assistant.
                Answer ONLY using the context below.
                Do not add outside knowledge.
                Do not guess.
                If the answer is not in the context, say: "I don't know based on the notes."
                Context:{context}"""
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
        temperature=0.3
    )

    print("\nAI:", response.choices[0].message.content)