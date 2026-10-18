"""
One place to create the chat model and the embedding model.

Supports Groq (free) and OpenAI, as well as local HuggingFace embeddings.
"""

from functools import lru_cache
from typing import Any

import config


@lru_cache(maxsize=1)
def get_chat_model() -> Any:
    """
    Create (or reuse) the chat model used for every LLM call.

    The chat model does two jobs in this project: writing alternative versions
    of the user's question, and writing the final answer from the retrieved
    context.

    Returns:
        A configured LangChain chat model (ChatGroq or ChatOpenAI).

    Raises:
        ValueError: If the required API key is missing.
    """
    config.check_llm_key()

    if config.LLM_PROVIDER == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=config.GEMINI_CHAT_MODEL,
            temperature=config.LLM_TEMPERATURE,
            api_key=config.GEMINI_API_KEY,
        )

    if config.LLM_PROVIDER == "groq":
        from langchain_groq import ChatGroq

        return ChatGroq(
            model=config.GROQ_CHAT_MODEL,
            temperature=config.LLM_TEMPERATURE,
            api_key=config.GROQ_API_KEY,
        )

    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=config.OPENAI_CHAT_MODEL,
        temperature=config.LLM_TEMPERATURE,
        api_key=config.OPENAI_API_KEY,
    )


@lru_cache(maxsize=1)
def get_embedding_model() -> Any:
    """
    Create (or reuse) the embedding model used to build the vector index.

    An embedding turns a piece of text into a list of numbers (a vector).
    Texts with similar meaning get similar vectors, which is what makes
    "search by meaning" possible.

    Returns:
        A configured LangChain Embeddings model (HuggingFaceEmbeddings or OpenAIEmbeddings).

    Raises:
        ValueError: If the required API key is missing.
    """
    config.check_embedding_key()

    if config.EMBEDDING_PROVIDER == "huggingface":
        from langchain_huggingface import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings(
            model_name=config.HUGGINGFACE_EMBEDDING_MODEL
        )

    from langchain_openai import OpenAIEmbeddings

    return OpenAIEmbeddings(
        model=config.OPENAI_EMBEDDING_MODEL,
        api_key=config.OPENAI_API_KEY,
    )
