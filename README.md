# 🎓 Smart Syllabus Chatbot

A smart academic chatbot that answers questions based on a given syllabus using a **local AI model**.

---

## 🚀 Features

* 📚 Ask questions related to your syllabus
* 🤖 Powered by local LLM (Phi-3 via Ollama)
* ⚡ Fast responses with optimized prompts
* 🎨 Modern UI built with Streamlit
* 🔒 Works completely offline

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Ollama (Local LLM runtime)
* Phi-3 Model

---

## 📂 Project Structure

```
syllabus-chatbot/
│── app.py
│── syllabus/
│   ├── year1.txt
│   ├── year2.txt
│   ├── year3.txt
│   └── year4.txt
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/syllabus-chatbot.git
cd syllabus-chatbot
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Install and run Ollama

Download Ollama from:
https://ollama.com

Then run:

```
ollama pull phi3
ollama run phi3
```

---

### 4️⃣ Run the app

```
streamlit run app.py
```

---

## 💡 How It Works

1. User selects year & asks a question
2. App loads relevant syllabus
3. Prompt is sent to Phi-3 via Ollama
4. AI generates a syllabus-based answer

---

## 🧠 Example Questions

* What topics are covered in DBMS?
* Explain operating systems syllabus
* What are key subjects in 3rd year?

---

## ⚠️ Notes

* Works best on systems with **4GB+ RAM**
* Uses optimized prompts for faster response
* Ensure Ollama is running before starting the app

---

## 📌 Future Improvements

* Chat history
* Voice input
* Web deployment
* Smarter syllabus search (RAG)

---

## 👩‍💻 Author

Thanvi R Shetty

---

## ⭐ If you like this project

Give it a star on GitHub!
