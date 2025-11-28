"""Configuration and constants"""

import os

# LangSmith Configuration
LANGSMITH_PROJECT = os.getenv("LANGCHAIN_PROJECT", "carbon-footprint-analyzer")

def get_langsmith_config():
    """Get LangSmith configuration for tracing"""
    return {
        "callbacks": [],
        "tags": ["carbon-footprint", "indian-bank-statement"],
        "metadata": {
            "version": "2.0",
            "features": ["pii-redaction", "hybrid-categorization", "min-max-ranges"]
        }
    }

# Default models
DEFAULT_OPENAI_MODEL = "gpt-4o"
DEFAULT_GROQ_MODEL = "llama-3.3-70b-versatile"