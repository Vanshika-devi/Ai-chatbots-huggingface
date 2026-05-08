from dotenv import load_dotenv
import streamlit as st
from huggingface_hub import InferenceClient
import pyttsx3
import threading
import os

# ---------------------------
# Hugging Face Client
# ---------------------------

load_dotenv()
client = InferenceClient(
    model="Qwen/Qwen2.5-7B-Instruct",
    token=os.getenv("HF_TOKEN")
)

# ---------------------------
# Streamlit Settings
# ---------------------------

st.set_page_config(
    page_title="AI Voice Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Voice Chatbot")

# ---------------------------
# Session State
# ---------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# prevent overlapping speech
if "speaking" not in st.session_state:
    st.session_state.speaking = False

# ---------------------------
# Voice Function
# ---------------------------

def speak(text):

    try:

        engine = pyttsx3.init()

        engine.setProperty('rate', 170)

        engine.setProperty('volume', 1.0)

        voices = engine.getProperty('voices')

        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)

        engine.say(text)

        engine.runAndWait()

        engine.stop()

    except Exception as e:

        print("Speech Error:", e)

# ---------------------------
# Show Chat History
# ---------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ---------------------------
# User Input
# ---------------------------

prompt = st.chat_input("Type your message...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                # Use FULL conversation history
                response = client.chat_completion(
                    messages=st.session_state.messages,
                    max_tokens=500,          # bigger responses
                    temperature=0.7,
                    top_p=0.9
                )

                ai_reply = response.choices[0].message.content

                # Display full response
                st.markdown(ai_reply)

                # Save AI response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_reply
                    }
                )

                # Speak response in background
                threading.Thread(
                    target=speak,
                    args=(ai_reply,),
                    daemon=True
                ).start()

            except Exception as e:

                st.error(f"Error: {e}")