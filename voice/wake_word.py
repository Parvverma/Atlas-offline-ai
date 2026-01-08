import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
import queue
import sys

MODEL_PATH = "C:/AI_ASSISTANT/models/vosk/vosk-model-small-en-us-0.15"
WAKE_WORD = "jarvis"

q = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen_for_wake_word():
    print("😴 ATLAS sleeping... say 'Atlas'")

    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, 16000)

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=audio_callback
    ):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if WAKE_WORD in text:
                    print("🟢 Wake word detected!")
                    return
