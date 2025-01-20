# Building a Custom Chatbot from Your Website Data using Large Language Model (LLM) and Langchain

This project is a an attempt to implement learning of LLMs and Langchain to build a multi-modal (text and voice) custom RAG based chatbot that answers customer queries related to Banking products - specifically Credit Card Products using the publicly available information on Bank's website. 

The chatbot helps users find suitable credit card product based on their needs. The bot provides detailed information about various credit card products offered by Wells Fargo, including cashback, travel rewards, business credit cards, and more. 

It uses both text and voice inputs to interact with customers, making it accessible and user-friendly, especially for those with disabilities. 


## Video demo
Please find the demo video [here](chatbotdemo_1.mp4).


## Features

- **Text Input and Output**: Allows users to interact with the bot using text as user input and receive text responses.
- **Voice Input and Output**: Allows users to interact with the bot using voice commands, making it more accessible and interactive.


## High Level Architecture
- To be added

## Tech Stack
- **Frontend**: Streamlit (Web UI for chatbot)
- **Backend**: Python
- **Voice Input/Output**: SpeechRecognition, pyttsx3
- **AI Model**: OpenAI API (for natural language processing)
- **Database**: Chroma Vector DB
- **Environment Management**: dotenv (for managing environment variables)
- **Framework for building Chatbot**: Langchain


## Libraries Used

- **streamlit**: For creating the interactive web interface.
- **openai**: For querying the OpenAI API to generate chatbot responses.
- **speech_recognition**: For voice input functionality.
- **pyttsx3**: For text-to-speech conversion, providing voice responses for the chatbot.
- **dotenv**: For managing environment variables, like the OpenAI API key.

