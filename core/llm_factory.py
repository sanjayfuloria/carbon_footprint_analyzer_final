"""LLM factory for different providers"""

import os
from .config import DEFAULT_OPENAI_MODEL, DEFAULT_GROQ_MODEL

def get_llm(provider: str = "openai", model: str = None, temperature: float = None, max_tokens: int = None):
    """
    Initialize LLM with choice between Groq and OpenAI
    
    Args:
        provider: "openai" or "groq"
        model: Specific model name (optional)
        temperature: Temperature for generation (optional, defaults per provider)
        max_tokens: Maximum tokens for generation (optional, defaults per provider)
    
    Returns:
        Configured LLM instance
    """
    if provider.lower() == "groq":
        from langchain_groq import ChatGroq
        
        if not model:
            model = DEFAULT_GROQ_MODEL
        
        return ChatGroq(
            model=model,
            temperature=temperature if temperature is not None else 0.1,
            max_tokens=max_tokens if max_tokens is not None else 4096,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
    
    elif provider.lower() == "openai":
        from langchain_openai import ChatOpenAI
        
        if not model:
            model = DEFAULT_OPENAI_MODEL
        
        return ChatOpenAI(
            model=model,
            temperature=temperature if temperature is not None else 0.1,
            max_tokens=max_tokens if max_tokens is not None else 4096,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    else:
        raise ValueError(f"Unsupported provider: {provider}. Choose 'openai' or 'groq'")
