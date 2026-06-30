from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage, 
    SystemMessage
)

# -----------------------------------
# Load Environment Variables
# -----------------------------------
load_dotenv()

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Gemini AI Chatbot")
st.caption("Powered by LangChain + Gemini")

# -----------------------------------
# Initialize Model
# -----------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# -----------------------------------
# Session State
# -----------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(
            content="You are a funny AI assistant."
        )
    ]

# -----------------------------------
# Display Chat History
# -----------------------------------
for message in st.session_state.chat_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# -----------------------------------
# Chat Input
# -----------------------------------
user_input = st.chat_input("Type your message...")

if user_input:

    # Show User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    # Generate Response
    response = llm.invoke(st.session_state.chat_history)

    # Store Response
    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )

    # Show AI Response
    with st.chat_message("assistant"):
        st.markdown(response.content)


# output command 
#.venv\Scripts\activate 
# streamlit run chatbot_UI.py    
