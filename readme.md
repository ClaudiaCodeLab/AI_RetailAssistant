# AI Shopping Assistant

Welcome to the AI Shopping Assistant! This project is a chatbot that helps customers find the best deals in a clothing store. It supports multiple AI models (Ollama, OpenAI, Claude) and is built using Gradio for an interactive interface.

---

## 🚀 Features
- 🛍️ Encourages customers to explore sale items (hats 60% off, most other items 50% off)
- 🤖 Supports multiple AI models (Ollama, OpenAI, Claude)
- 🔧 Easily configurable with environment variables
- 📡 Uses streaming responses for a smooth experience
- 🧪 Includes unit tests with `pytest`

---

## 📂 Project Structure
```
assistant_project/
│── src/
│   │── models/         # AI model implementations
│   │   │── base.py      # Abstract base class
│   │   │── ollama.py    # Ollama model integration
│   │   │── openai.py    # OpenAI model integration
│   │   │── claude.py    # Claude model integration
│   │── config/
│   │   └── settings.py  # Configuration settings
│   │── chat/
│   │   │── chatbot.py   # Chatbot logic
│   │   └── prompts.py   # Prompt templates
│   │── app.py           # Main application entry point
│   │── requirements.txt  # Dependencies
│   └── .env             # Environment variables
│── tests/
│   └── test_chatbot.py  # Unit tests
│── README.md            # Project documentation
└── .gitignore           # Ignore unnecessary files
```

---

## 🛠️ Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/ai-shopping-assistant.git
cd ai-shopping-assistant
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory:
```
API_KEY=ollama
OLLAMA_API_URL=http://localhost:11434/v1
MODEL=llama3.2
DEFAULT_PROVIDER=ollama
OPENAI_API_KEY=your_openai_key_here
CLAUDE_API_KEY=your_claude_key_here
```

---

## ▶️ Running the Application
Start the chatbot with:
```sh
python src/app.py
```
The Gradio UI will launch, and you can chat with the assistant!

---


## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a Pull Request

---

## 📜 License
This project is open-source under the [MIT License](LICENSE). Feel free to use and modify it!

---

## 📞 Contact
For questions or suggestions, feel free to reach out!
- ✉️ Email: your_email@example.com
- 🐙 GitHub: [yourusername](https://github.com/yourusername)

