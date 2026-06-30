"""Structure prompt
Cinesage analytics is a media intelligence company that helps straming platforms and production houses organize and analyses large volumes of movie data.
Every day, the company receives:
Movie descriptions, Press release, Blog articles, review summaries, metadata from multiple sources.
 But the problem is: the information is messy. Its unstructured and it comes in long paragraphs.
Streaming platform requires structure movie metadata, yet most incoming data arrives as messy paragraphs. Extracting it manually is time consuming, expensive, error-prone ad difficult to scale.
Cinesage wants to build an AI-powered tool that:
1.Takes a raw paragraph about a movie
2.extracts important structured information
3.generates a clean summary
4.returns it in JSON format
5.stores it in their datadase
"""
"""
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (Make sure GOOGLE_API_KEY is in your .env file)
load_dotenv()

# 1. Initialize the model with the correct spelling
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# 2. Define the structured prompt template
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system", #role to system
        "You are a helpful AI assistant. Your task is to provide clear, "
        "concise answers and format your responses using clean Markdown structure."
    ),
    (
        "user", 
        "{user_input}"
    )
])

# 3. Combine the prompt and model into a chain
chain = prompt_template | model

# 4. Invoke the chain by passing the variables
response = chain.invoke({"user_input": "Hello! Tell me one interesting space fact."})

print(response.content)
"""

import os
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# ==========================================
# 1. DEFINE THE DESIRED JSON STRUCTURE
# ==========================================
class MovieMetadata(BaseModel):
    title: str = Field(description="The official title of the movie.")
    release_year: Optional[int] = Field(description="The year the movie was released. Null if unknown.")
    genres: List[str] = Field(description="List of genres associated with the movie.")
    director: Optional[str] = Field(description="The director of the movie.")
    cast: List[str] = Field(description="Main actors or cast members mentioned.")
    key_themes: List[str] = Field(description="Key themes, tropes, or moods extracted from the text.")
    clean_summary: str = Field(description="A concise, professional 2-3 sentence summary of the movie's plot based on the text.")

# ==========================================
# 2. SETUP THE MODEL AND PROMPT
# ==========================================
# Initialize Gemini
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.1)

# Bind the model to our Pydantic schema to force JSON output
structured_llm = model.with_structured_output(MovieMetadata)

# Create the structured prompt template
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert media intelligence AI for Cinesage Analytics. "
        "Your task is to analyze messy, unstructured raw text about a movie, "
        "extract the required metadata fields accurately, and generate a clean plot summary."
    ),
    (
        "user",
        "Analyze the following raw text data:\n\n{raw_text}"
    )
])

# Chain them together
extraction_chain = prompt_template | structured_llm

# ==========================================
# 3. TEST THE SOLUTION
# ==========================================
messy_paragraph = """
Yesterday at the festival we caught a glimpse of Neo-Noir's latest darling. Directed by 
the visionary Elena Rostova, 'Shadows in the Neon' is an absolute cyberpunk trip. Set to hit 
theaters or streaming late 2025 or early 2026, it stars Marcus Vance as a grizzled cyber-detective 
and Aisha Kim as an rogue AI hologram. It's essentially a gritty sci-fi detective thriller 
dealing with themes of corporate greed, human identity, and memory manipulation. The plot follows 
Vance trying to track down a deleted consciousness in a rain-soaked futuristic Neo-Seoul.
"""

# Invoke the chain
try:
    extracted_data = extraction_chain.invoke({"raw_text": messy_paragraph})
    
    # This is now a validated Pydantic object
    print("--- EXTRACTED OBJECT ---")
    print(extracted_data)
    
    # Convert directly to standard JSON string for your database
    json_output = extracted_data.model_dump_json(indent=2)
    print("\n--- READY FOR DATABASE (JSON) ---")
    print(json_output)

except Exception as e:
    print(f"Extraction failed: {e}")