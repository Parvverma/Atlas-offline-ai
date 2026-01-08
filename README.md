# ATLAS — Offline AI Personal Assistant 🤖

ATLAS is a fully offline, privacy-focused AI personal assistant built in Python.
It supports voice and text interaction, permanent memory, safe system automation,
and runs entirely on the user's local machine.

---

## ✨ Features

- 🧠 Offline Large Language Model (no internet required)
- 🎙 Voice input (Speech-to-Text)
- 🔊 Voice output (Text-to-Speech)
- 💬 Desktop chat UI (Tkinter)
- 💤 Wake word: "Atlas"
- 🧠 Permanent memory (local JSON storage)
- 📂 Safe file & app control (whitelisted)
- 🖥 One-click executable (optional)
- 🔐 Privacy-first (no cloud, no tracking)

---

## 🧠 AI Models Used

### 1️⃣ Language Model (Brain)
- **Phi-3**
- Runs locally via **Ollama**
- Optimized for CPU usage
- Fast response, low memory footprint

### 2️⃣ Wake Word Detection
- **Vosk (offline speech recognition)**
- Used only for detecting "Atlas"
- Lightweight and always offline

### 3️⃣ Voice Recognition
- **Whisper (base model)**
- Converts voice commands to text
- Fully offline

### 4️⃣ Voice Output
- **pyttsx3**
- Uses system TTS engine
- No internet required

---

## 🧩 Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| AI Runtime | Ollama |
| UI | Tkinter |
| Wake Word | Vosk |
| STT | Whisper |
| TTS | pyttsx3 |
| Automation | Python OS & subprocess |
| Memory | JSON (local) |

---

## 📁 Project Structure

AI_ASSISTANT/
│
├── core/ # Main logic, memory
├── ui/ # Desktop UI
├── voice/ # Voice input, output, wake word
├── commands/ # Safe automation
├── models/ # Model placeholders (not included)
├── README.md
├── requirements.txt
└── .gitignore


---

## 🚀 Installation & Setup

### 1️⃣ Install Python (3.10+ recommended)

https://www.python.org/downloads/

Make sure to check **Add Python to PATH**.

---

### 2️⃣ Install Ollama

https://ollama.com

Download and install for Windows.

---

### 3️⃣ Download AI Model

```bash
ollama pull phi3

4️⃣ Install Python Dependencies
pip install -r requirements.txt

5️⃣ Run ATLAS
python -m core.main

Say "Atlas" to activate.


🔐 Privacy & Safety

No cloud APIs

No data leaves your machine

No background recording

File access is restricted to safe directories only

Memory is stored locally and can be deleted anytime


📌 Notes

AI models are NOT included in the repository

Models are downloaded automatically via Ollama

This project is for educational and personal use


👨‍💻 Author

Built by Parv Verma
First-year B.Tech student
Passionate about AI, Robotics, and Systems Engineering

⭐ If you like this project

Give it a star ⭐ and feel free to fork!