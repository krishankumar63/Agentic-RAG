from langchain_groq import ChatGroq
from app.config import settings


portkey_client = None


def get_langchain_llm(feature: str = "rag") -> ChatGroq:
    """
    Return a direct Groq-backed LangChain client.

    This bypasses the failing Portkey gateway and uses the Groq API key directly.
    The rest of the app can keep using the same LangChain interface.
    """
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.GROQ_MODEL,
        temperature=0,
    )


def extract_cache_status(response) -> str:
    """Compatibility helper retained for the old gateway integration path."""
    return "MISS"