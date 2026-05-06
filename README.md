# 🤖 AI Voice Chatbot

A professional AI-powered conversational chatbot built using **Streamlit**, **Hugging Face Inference API**, and **pyttsx3** for real-time voice-enabled interactions.

The application provides an interactive chat interface with conversational memory, AI-generated responses, and speech synthesis capabilities for a more engaging user experience.

---

# 📌 Features

- 💬 Real-time AI chatbot interface
- 🧠 Context-aware conversation memory
- 🔊 Voice responses using text-to-speech
- ⚡ Fast AI inference with Hugging Face
- 🎨 Clean and modern Streamlit UI
- 🧵 Background speech processing
- 🔒 Secure API token management
- 📱 Lightweight and responsive application

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Frontend web interface |
| Hugging Face Hub | AI model inference |
| pyttsx3 | Offline text-to-speech engine |
| threading | Background task execution |

---

# 📂 Project Structure

```bash
AI-Voice-Chatbot/
│
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# 🚀 Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Voice-Chatbot.git

cd AI-Voice-Chatbot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Add the following dependencies to `requirements.txt`

```txt
streamlit
huggingface_hub
pyttsx3
python-dotenv
```

---

# 🔑 Environment Variables Setup

## Create a `.env` file

```env
HF_TOKEN=your_huggingface_api_token
```

---

# 🔒 Important Security Note

Never expose API keys publicly on GitHub.

Always:
- Store secrets inside `.env`
- Add `.env` to `.gitignore`
- Revoke exposed tokens immediately

---

# 📝 .gitignore

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

---

# ▶️ Running the Application

Start the Streamlit server:

```bash
streamlit run chatbot.py
```

The application will open in your browser automatically.

---

# 🧠 AI Model

This project uses:

## Qwen/Qwen2.5-7B-Instruct

Hosted on Hugging Face Inference API.

### Capabilities

- Conversational AI
- Context retention
- Coding assistance
- Creative writing
- Question answering
- General AI interaction

---

# 🔊 Voice Assistant Functionality

The chatbot includes speech synthesis using `pyttsx3`.

### Features

- Adjustable speech rate
- Voice selection
- Volume control
- Offline speech generation

---

# 🧵 Background Threading

Speech synthesis runs in a separate thread to ensure the Streamlit UI remains responsive.

```python
threading.Thread(
    target=speak,
    args=(ai_reply,),
    daemon=True
).start()
```

---

# 💡 Application Workflow

1. User enters a message
2. Message is stored in session history
3. AI model processes the request
4. Response is generated
5. Response displayed on screen
6. AI response spoken aloud

---

# ⚙️ Core Functionalities

## ✅ Session State Memory

Maintains conversation history throughout the session.

```python
st.session_state.messages
```

---

## ✅ Chat Interface

Uses Streamlit chat components:

```python
st.chat_input()

st.chat_message()
```

---

## ✅ AI Inference

Handles response generation through Hugging Face API.

```python
client.chat_completion()
```

---

# 🐞 Error Handling

The project includes exception handling for:

- API request failures
- Voice engine issues
- Runtime errors
- Invalid responses

Example:

```python
except Exception as e:
    st.error(f"Error: {e}")
```

---

# 🌟 Future Enhancements

Planned improvements include:

- 🎤 Speech-to-text support
- 🌐 Multi-language support
- 🧠 Persistent memory storage
- 📄 Chat export feature
- ☁️ Cloud deployment
- 🔐 User authentication
- 🎭 Custom AI personalities

---

# ☁️ Deployment Platforms

This project can be deployed on:

- Streamlit Cloud
- Hugging Face Spaces
- Render
- Railway
- AWS
- Azure
- Heroku

---

# 📸 User Interface Preview

The application provides:

- Interactive messaging UI
- Real-time AI responses
- Smooth voice interaction
- Clean responsive design

---

# 📈 Performance Highlights

- Lightweight architecture
- Fast inference responses
- Responsive UI experience
- Efficient memory handling

---

# 👩‍💻 Author

### Vanshika Devi

AI & Python Developer

---

# 📄 License

This project is licensed under the MIT License.

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 📢 Share with others

---

# 📬 Contact

For suggestions, improvements, or collaboration opportunities:

- GitHub: https://github.com/your-username

---

# 🚀 AI Voice Chatbot

Building intelligent conversational experiences with AI and voice technology.
