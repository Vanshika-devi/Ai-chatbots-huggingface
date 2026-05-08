from huggingface_hub import InferenceClient
import pyttsx3
import os
from dotenv import load_dotenv
load_dotenv()
client = InferenceClient(
    model="Qwen/Qwen2.5-7B-Instruct",
    token=os.getenv("HF_TOKEN")
)
#ollama run llama3 free models next model with them
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

print("--- AI Voice Chatbot ---")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    try:

        response = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            max_tokens=100
        )

        ai_reply = response.choices[0].message.content

        speak(ai_reply)

    except Exception as e:
        print("Error:", e)