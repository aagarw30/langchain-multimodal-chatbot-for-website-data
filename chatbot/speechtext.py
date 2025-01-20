import speech_recognition as sr
from gtts import gTTS
import pyaudio
import wave

def record_audio():
    audio = pyaudio.PyAudio();
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass
    stream.stop_stream()
    stream.close()
    audio.terminate()
    sound_file = wave.open("my_recording.wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()



def speech_to_text(audio_file = "my_recording.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            # Use Google Web Speech API
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Speech was not understood."
        except sr.RequestError as e:
            return f"Could not request results; {e}"



def text_to_speech(text, output_file='response.wav'):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"Audio saved to {output_file}")