from huggingface_hub import InferenceClient
import pyttsx3
import os
from dotenv import load_dotenv
load_dotenv()
client = InferenceClient(
    model="Qwen/Qwen2.5-7B-Instruct",
    token=os.getenv("HF_TOKEN")
)
# Hugging Face AI model
# Voice function
def speak(text):

    print("\nAI:", text)

    # create fresh engine every time
    engine = pyttsx3.init()

    # voice settings
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    # speak
    engine.say(text)

    engine.runAndWait()

    engine.stop()


print("\n--- AI Voice Chatbot Started ---")
print("Type 'exit' to quit.\n")

while True:

    # user input
    user_input = input("You: ")

    # exit
    if user_input.lower() == "exit":

        speak("Goodbye!")

        break

    try:

        # AI response
        response = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            max_tokens=150
        )

        # extract reply
        ai_reply = response.choices[0].message.content

        # speak + print
        speak(ai_reply)

    except Exception as e:

        print("\nError:", e)