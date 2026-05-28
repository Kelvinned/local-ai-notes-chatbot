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
    stop_words = ["what", "is", "are", "the", "a", "an", "about", "do", "does", "my", "notes", "say", "speak", "tell", "me"]

    question_words = question.lower().split()
    important_words = []

    for word in question_words:
        if word not in stop_words:
            important_words.append(word)

    relevant_chunks = []

    for chunk in chunks:
        chunk_lower = chunk.lower()

        for word in important_words:
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