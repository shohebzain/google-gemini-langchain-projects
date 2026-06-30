import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 1. Load the environment variables securely from .env
load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    raise ValueError("Google API Key missing! Check your .env file.")

# 2. Safely initialize Google Gemini using LangChain's uniform string
model = init_chat_model("google_genai:gemini-2.5-flash") 

# 3. Test your prompt
try:
    response = model.invoke("Mohammad Shoheb")
    print(response.content)
except Exception as e:
    print(f"An error occurred: {e}")
