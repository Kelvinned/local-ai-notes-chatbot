from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key='lm-studio'
)

with open ("notes.txt",'r') as file:
    notes = file.read()

messages=[{
    "role":"system",
    "content":f"You are a helpful study assistant. Explain clearly and briefly using these notes:\n\n{notes}."
}]
while True:
    user_question = input("\nAsk Something:")

    if user_question.lower() in ["exit", "quit","q"]:
        print("Goodbye")
        break
    #memory
    messages.append({"role": "user", "content": user_question})

    response = client.chat.completions.create(
        model= "llama-3.2-3b-instruct",
        messages=messages,
        temperature=0.7,
    )

    answer = response.choices[0].message.content
    print("\nAI:", answer)

    messages.append({"role": "assistant", "content": answer})   




