import threading
import tkinter as tk
from tkinter import scrolledtext
from ollama import chat
from voice.listen import listen
from voice.speak import speak
from core.memory import load_memory, save_memory
from commands.file_ops import open_path
from commands.app_ops import open_app

# ====== THEME COLORS ======
BG_COLOR = "#0b0f14"        # deep space black
CHAT_BG = "#0f1623"        # dark navy
USER_COLOR = "#00e676"     # neon green (you)
AI_COLOR = "#00b0ff"       # Jarvis blue
TEXT_COLOR = "#e0e0e0"
BTN_COLOR = "#102027"      # dark tech panel


# ====== MEMORY ======
memory = load_memory()
messages = [
    {
        "role": "system",
        "content": (
            "You are JARVIS, a calm, intelligent, helpful personal AI assistant. "
            "You speak clearly, politely, and concisely. "
            "You assist with explanations, tasks, and problem solving. "
            "You are offline and respect user privacy."
        )
    }
] + memory["chat_history"]


def add_chat(text, sender="AI"):
    chat_box.config(state=tk.NORMAL)
    if sender == "You":
        chat_box.insert(tk.END, "You: ", "user")
    else:
        chat_box.insert(tk.END, "AI: ", "ai")

    chat_box.insert(tk.END, text + "\n\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

def handle_command(text):
    t = text.lower()
    if "open notepad" in t:
        return open_app("notepad")
    if "open calculator" in t:
        return open_app("calculator")
    if t.startswith("open "):
        return open_path(t.replace("open ", "").strip())
    return None

# def send_text(event=None):
#     user_input = entry.get().strip()
#     if not user_input:
#         return

#     entry.delete(0, tk.END)
#     add_chat(user_input, "You")

#     messages.append({"role": "user", "content": user_input})

#     cmd = handle_command(user_input)
#     if cmd:
#         add_chat(cmd, "AI")
#         speak(cmd)
#         return

#     response = chat(model="phi3", messages=messages)
#     ai_reply = response.message.content

#     messages.append({"role": "assistant", "content": ai_reply})
#     memory["chat_history"] = messages
#     save_memory(memory)

#     add_chat(ai_reply, "AI")
#     speak(ai_reply)

def send_text(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return

    entry.delete(0, tk.END)
    add_chat(user_input, "You")

    threading.Thread(target=process_ai, args=(user_input,)).start()

def process_ai(user_input):
    messages.append({"role": "user", "content": user_input})

    cmd = handle_command(user_input)
    if cmd:
        add_chat(cmd, "AI")
        speak(cmd)
        return

    response = chat(model="phi3", messages=messages)
    ai_reply = response.message.content

    messages.append({"role": "assistant", "content": ai_reply})
    memory["chat_history"] = messages
    save_memory(memory)

    add_chat(ai_reply, "AI")
    speak(ai_reply)



def speak_input():
    add_chat("Listening...", "AI")
    root.update()

    user_input = listen()
    add_chat(user_input, "You")

    messages.append({"role": "user", "content": user_input})

    response = chat(model="phi3", messages=messages)
    ai_reply = response.message.content

    messages.append({"role": "assistant", "content": ai_reply})
    memory["chat_history"] = messages
    save_memory(memory)

    add_chat(ai_reply, "AI")
    speak(ai_reply)

def start_ui():
    global root, chat_box, entry

    root = tk.Tk()
    root.title("JARVIS")
    root.geometry("520x600")
    root.configure(bg=BG_COLOR)

    chat_box = scrolledtext.ScrolledText(
        root,
        bg=CHAT_BG,
        fg=TEXT_COLOR,
        wrap=tk.WORD,
        state=tk.DISABLED,
        font=("Segoe UI", 10)
    )
    chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    chat_box.tag_config("user", foreground=USER_COLOR)
    chat_box.tag_config("ai", foreground=AI_COLOR)

    bottom_frame = tk.Frame(root, bg=BG_COLOR)
    bottom_frame.pack(fill=tk.X, padx=10, pady=10)

    entry = tk.Entry(
        bottom_frame,
        bg=CHAT_BG,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        font=("Segoe UI", 10)
    )
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    entry.bind("<Return>", send_text)

    send_btn = tk.Button(
        bottom_frame,
        text="Send",
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        command=send_text
    )
    send_btn.pack(side=tk.RIGHT)

    speak_btn = tk.Button(
        root,
        text="🎙 Speak",
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        command=speak_input
    )
    speak_btn.pack(pady=(0, 10))

    start_message = ("Hello, I am JARVIS.\n"
    "Your offline personal AI assistant.\n\n"
    "• Voice enabled\n"
    "• Memory active\n"
    "• Systems ready\n\n"
    "How may I assist you?")
    add_chat(start_message, "AI")

    root.mainloop()
