#chatbot without histroy
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env
load_dotenv()

# Initialize Gemini model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

print("🤖 Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chat_model.invoke(user_input)

    print(f"Bot: {response.content}\n")