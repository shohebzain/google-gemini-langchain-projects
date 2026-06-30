from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv()

message = [
    SystemMessage(content="you are a funny AI agent") #role to AI
]
# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Interaction History
chat_history = []

print("=" * 60)
print("🤖 Gemini Chatbot with Interaction History")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("\nBot : Goodbye 👋")
        break

    # Store user message
    chat_history.append(HumanMessage(content=user_input))

    # Send complete history to model
    response = llm.invoke(chat_history)
    
    # Store AI response
    chat_history.append(AIMessage(content=response.content))

    # Print response
    print("\nBot :", response.content)

"""
Problem with current short-term memory
•	No role separation (no system / user/ assistant distinction)
•	Just raw strings -> weak conversation structure
•	Memory keeps growing infinitely
•	Will hit token limit
•	API cost increases as history grows 
•	No trimming mechanisms
•	No summarization of old chats
•	Not production scalable 
•	No control over context window

"""