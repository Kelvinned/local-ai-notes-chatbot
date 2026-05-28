from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def load_notes():
    with open("notes.txt", "r") as file:
        return file.read()

def split_into_chunks(text):
    return text.split("\n\n")

def find_relevant_chunks(question, chunks):
    stop_words = ["what", "is", "are", "the", "a", "an", "about", "do", "does", "my", "notes", "say", "speak", "tell", "me", "between", "and", "difference"]

    question_words = question.lower().replace("?", "").split()
    important_words = []

    for word in question_words:
        if word not in stop_words:
            important_words.append(word)

    scored_chunks = []

    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = 0

        for word in important_words:
            if word in chunk_lower:
                score += 1

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    relevant_chunks = []

    for score, chunk in scored_chunks:
        relevant_chunks.append(chunk)

    return relevant_chunks[:5]

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
        messages=[{"role": "system",
                   "content": f"""You are a strict notes assistant.
                   Use ONLY the context below to answer.
                   The context below is already selected from the user's notes.
                   If the context contains information related to the question, answer using that information.
                   Do not use outside knowledge.
                   If the context is empty or unrelated, say: "The topic isn't discussed in the notes."
                   Context:{context}"""},
                   {"role": "user","content": user_question}],temperature=0.1)
    

    print("\nAI:", response.choices[0].message.content)