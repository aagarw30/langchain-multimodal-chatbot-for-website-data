import os
import streamlit as st
from dotenv import load_dotenv
from utils import get_response  # Replace with your function to get chatbot response

# Load environment variables
load_dotenv('../env.sh')  # Update the path if necessary

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

    # Input for user message
    user_input = st.chat_input("Ask about our Credit Cards...")

    # Add the user message and assistant response to the history
    if user_input:
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Display a spinner while fetching the response
        with st.spinner("Fetching information..."):
            # Get chatbot response
            response = get_response(user_input)  # Replace with your function to generate a response

        # Add assistant's response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    # Display chat history after user input and assistant response
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Assistant:** {message['content']}")

if __name__ == "__main__":
    main()
