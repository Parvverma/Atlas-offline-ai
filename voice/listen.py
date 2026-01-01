import sounddevice as sd
from scipy.io.wavfile import write
import whisper

model = whisper.load_model("base")

def listen():
    fs = 16000
    print("Listening... Speak now")

    audio = sd.rec(int(5 * fs), samplerate=fs, channels=1)
    sd.wait()

    write("voice_input.wav", fs, audio)

    result = model.transcribe("voice_input.wav")
    return result["text"]