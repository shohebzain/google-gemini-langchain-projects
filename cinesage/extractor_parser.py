from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# 1. Define your data structure
class MovieMetadata(BaseModel):
    title: str = Field(description="The official title of the movie.")
    release_year: Optional[int] = Field(description="The year the movie was released.")
    genres: List[str] = Field(description="List of genres associated with the movie.")
    director: Optional[str] = Field(description="The director of the movie.")
    cast: List[str] = Field(description="Main actors or cast members mentioned.")
    clean_summary: str = Field(description="A concise 2-3 sentence summary of the movie.")

# 2. Set up the Pydantic Output Parser
parser = PydanticOutputParser(pydantic_object=MovieMetadata)

# 3. Create the prompt, injecting the parser's formatting instructions
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert media intelligence AI for Cinesage Analytics.\n"
        "Your task is to extract structured metadata from raw text.\n\n"
        "{format_instructions}"  # The parser will inject schema rules here
    ),
    (
        "user",
        "Extract the metadata from this text:\n\n{raw_text}"
    )
])

# 4. Initialize Gemini
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.1)

# 5. Chain them together: Prompt -> Model -> Parser
chain = prompt_template | model | parser

# ==========================================
# TEST THE PARSER
# ==========================================
messy_paragraph = """
Directed by the visionary Elena Rostova, 'Shadows in the Neon' (2025) is an absolute cyberpunk trip. 
It stars Marcus Vance as a grizzled cyber-detective. It's a sci-fi detective thriller.
"""

# We must pass both the raw text AND the parser's format instructions
result = chain.invoke({
    "raw_text": messy_paragraph,
    "format_instructions": parser.get_format_instructions()
})

# 'result' is now a fully validated Pydantic object
print(result.title)          # Output: Shadows in the Neon
print(result.model_dump_json(indent=2))  # Ready for your database!