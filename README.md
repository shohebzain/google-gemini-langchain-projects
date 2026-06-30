<div align="center">

# 🤖 Google Gemini & LangChain Projects

### 🚀 Build Production-Ready AI Applications with Google Gemini & LangChain

<p align="center">
A collection of hands-on AI projects demonstrating chatbots, embeddings, structured outputs, prompt engineering, and modern LLM application development using Google Gemini, LangChain, and Python.
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white"/>

<img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>

</p>

</div>

---

## 📂 Project Directory Structure

```
d:\Gen AI\
│
├── chatbots/
│   ├── cli_basic.py             # CLI-based chatbot without conversation history
│   ├── cli_with_history.py      # CLI-based chatbot with in-memory conversation history
│   └── streamlit_app.py         # Web-based chatbot UI built using Streamlit
│
├── cinesage/
│   ├── extractor_structured.py  # Movie metadata extractor using Gemini's native structured output
│   └── extractor_parser.py      # Movie metadata extractor using LangChain's PydanticOutputParser
│
├── embeddings/
│   └── generate_embeddings.py    # Vector generation for text & documents using Gemini Embeddings
│
├── quickstarts/
│   ├── test_api.py              # Initial connectivity check for Gemini using uniform model strings
│   └── check_version.py         # Utility script to check the installed LangChain version
│
├── .env                         # Application environment keys (not committed)
├── .python-version              # Local python environment specification
├── pyproject.toml               # Modern Python project configuration
└── requirements.txt             # Python project dependencies
```

---

## 🛠️ Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.13 or newer installed.

### 2. Configure Local Environment
Clone the project and initialize a virtual environment:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On Windows (cmd):
.venv\Scripts\activate.bat
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies
Install all package dependencies defined in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Setup API Keys
Create a `.env` file in the project root directory and add your Google API key:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## 🚀 How to Run the Applications

### 🔹 Quickstarts

To verify installation and connection to the Google Gemini API:

```bash
# Verify the LangChain package version
python quickstarts/check_version.py

# Test standard Gemini API invocation
python quickstarts/test_api.py
```

### 🔹 Chatbots

This folder includes multiple interactive chatbots ranging from basic terminal execution to a Streamlit web interface.

#### 1. Basic CLI Chatbot (Stateless)
A stateless chatbot that responds to user inputs but does not store context.
```bash
python chatbots/cli_basic.py
```

#### 2. Advanced CLI Chatbot (With Memory)
Maintains a full in-memory conversation history to carry context across multiple interactions.
```bash
python chatbots/cli_with_history.py
```

#### 3. Web UI Chatbot (Streamlit)
A modern, rich web browser interface powered by Streamlit that features chat history, dynamic formatting, and an elegant layout.
```bash
streamlit run chatbots/streamlit_app.py
```

---

### 🔹 Embeddings Generation

Generate semantic vector representations of text. Includes examples for embedding single text sentences and batch-embedding list documents.

```bash
python embeddings/generate_embeddings.py
```

---

### 🔹 CineSage Media Extraction Tool

A media intelligence module that parses unstructured movie descriptions or raw paragraphs and transforms them into strict, database-ready JSON schemas.

#### 1. Native Structured Output Extractor
Utilizes LangChain's native `.with_structured_output()` API wrapper to constrain model outputs.
```bash
python cinesage/extractor_structured.py
```

#### 2. Pydantic Parser Extractor
Utilizes LangChain's `PydanticOutputParser` to inject formatting instructions into system prompts and validate returned JSON responses.
```bash
python cinesage/extractor_parser.py
```

---

## 📦 Principal Libraries Used

* **[LangChain Core & Community](https://github.com/langchain-ai/langchain)**: Core frameworks for prompt orchestration, chains, schemas, and chat models.
* **[LangChain Google GenAI](https://github.com/langchain-ai/langchain-google)**: Direct wrapper integration for Gemini's models (`gemini-2.5-flash`, `models/gemini-embedding-001`).
* **[Pydantic](https://docs.pydantic.dev/)**: Class schemas defining structures for data extraction and auto-validation.
* **[Streamlit](https://streamlit.io/)**: Fast, Python-native UI prototyping framework for machine learning applications.
* **[python-dotenv](https://github.com/theofidry/django-dotenv)**: Secure API key configuration loader.
