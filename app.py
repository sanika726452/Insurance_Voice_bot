import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
from bot import get_response, get_all_questions

def speak(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        tts.save(f.name)
        audio_path = f.name
    audio_bytes = open(audio_path, 'rb').read()
    os.remove(audio_path)
    st.audio(audio_bytes, format='audio/mp3')

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak.")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        st.success(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, could not understand.")
    except sr.RequestError:
        st.error("Speech recognition service unavailable.")
    return ""

st.title("🛡️ Insurance Voice/Text Assistant")

# Sample questions dropdown
questions = get_all_questions()
selected = st.selectbox("📋 Sample Questions", [""] + questions)

user_input = ""
if selected:
    user_input = selected

typed_input = st.text_input("Or type your question:")
if typed_input:
    user_input = typed_input

if st.button("🎤 Speak"):
    user_input = listen()

if user_input:
    st.write(f"**You:** {user_input}")
    response = get_response(user_input)
    st.write(f"**Bot:** {response}")
    speak(response)
