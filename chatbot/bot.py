import os
import streamlit as st
from dotenv import load_dotenv
from utils import get_response  # Replace with your function to get chatbot response
import speech_recognition as sr
import pyttsx3
import time

# Load environment variables
load_dotenv('../env.sh')  # Update the path if necessary

def get_voice_input():
    """
    Captures voice input from the user's microphone and returns the transcribed text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_placeholder = st.empty()

        status_placeholder.info("Listening... Please speak now.")
        
        # Adjust for ambient noise
        # recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=20)
            status_placeholder.empty()
            status_placeholder.success("Processing your voice input...")
            time.sleep(1)  # Simulate processing time

            text = recognizer.recognize_google(audio)
            status_placeholder.empty()
            status_placeholder.success(f"Transcribed Voice Input: {text}")
            time.sleep(2)  # Allow user to see transcription before it disappears
            status_placeholder.empty()
            return text

        except sr.UnknownValueError:
            status_placeholder.empty()
            st.warning("Sorry, I could not understand the audio. Please try again.")
        except sr.RequestError:
            status_placeholder.empty()
            st.error("There was an error with the speech recognition service. Please try again.")
        except sr.WaitTimeoutError:
            status_placeholder.empty()
            st.warning("You didn't say anything. Please try again.")
        return ""

def speak_response(response):
    """
    Converts text response to speech for accessibility purposes.
    """
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

def main():
    # Load OpenAI API Key
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Check if the key is available in the environment
    if not openai_api_key:
        st.error("OpenAI API key not found. Please set the environment variable `OPENAI_API_KEY`.")
        return

    # Page configuration
    st.set_page_config(
        page_title="Product Chatbot",
        page_icon="💳",
        layout="wide"
    )

    # Main title
    st.title("💳 Fargo.ai")
    st.write("Hello, I am Your AI Assistant. Let me help you find the perfect credit card product for your needs!")

    # Initialize session state for chat history if not already set
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Check if the last input was from voice
    if 'voice_mode' not in st.session_state:
        st.session_state.voice_mode = False

    # Input area with columns layout (Text box 4:1 Voice button)
    st.markdown('<div style="position: fixed; bottom: 60px; width: 100%;">', unsafe_allow_html=True)
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.chat_input("Ask about our Credit Cards...")
    with col2:
        if st.button("🎤 Voice Input"):
            voice_input = get_voice_input()
            if voice_input:
                user_input = voice_input
                st.session_state.voice_mode = True  # Track that voice was used

    st.markdown('</div>', unsafe_allow_html=True)

    # Process user input and get response
    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.spinner("Fetching information..."):
            response = get_response(user_input)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        # Speak the response only if the user used voice input
        if st.session_state.voice_mode:
            speak_response(response)
            st.session_state.voice_mode = False  # Reset for next input

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Assistant:** {message['content']}")

if __name__ == "__main__":
    main()