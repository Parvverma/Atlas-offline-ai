# from ollama import chat
# from voice.listen import listen
# from voice.speak import speak

# print("🎙 Speak to your AI...")

# user_text = listen()
# print("You said:", user_text)

# response = chat(
#     model="mistral",
#     messages=[{"role": "user", "content": user_text}]
# )

# ai_text = response.message.content
# print("AI says:", ai_text)

# speak(ai_text)

#|| \****\ || 

# from ui.app import start_ui

# if __name__ == "__main__":
#     start_ui()

#|| \****\ ||

from voice.wake_word import listen_for_wake_word
from ui.app import start_ui

if __name__ == "__main__":
    listen_for_wake_word()
    start_ui()
