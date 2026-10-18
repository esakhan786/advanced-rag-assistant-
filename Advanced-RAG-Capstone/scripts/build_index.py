"""
Build the vector database from everything in `data/documents`.

Run it with:
    python scripts/build_index.py

This does exactly what the "Build Vector DB" button in the Streamlit sidebar
does. Having it as a script is handy for a first-time setup, because you can
index the documents once before you ever open the UI.

Warning: this replaces any existing index.
"""

import logging
import sys
from pathlib import Path

# Lets this script import `config` and `src` when run from anywhere.
sys.path.insert(0, str(Path(__file__).parent.parent))

import config  # noqa: E402
from src.indexing import build_index  # noqa: E402
from src.ingestion import load_documents_from_folder  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def main() -> None:
    """
    Load the documents folder, split it and build the index from scratch.

    Prints a short summary so you can see how many chunks were created. Any
    failure (missing API key, empty folder) is reported as a readable message
    rather than a stack trace.
    """
    print(f"Reading documents from: {config.DOCUMENTS_DIR}")

    documents = load_documents_from_folder(config.DOCUMENTS_DIR)
    if not documents:
        print("No readable documents found. Add PDF, TXT or DOCX files and try again.")
        return

    try:
        stats = build_index(documents)
    except Exception as error:
        print(f"Build failed: {error}")
        return

    print("\nIndex built successfully.")
    print(f"  Pages / documents loaded : {stats['documents']}")
    print(f"  Parent chunks (context)  : {stats['parents']}")
    print(f"  Child chunks (searched)  : {stats['children']}")
    print(f"  Vector database          : {config.VECTOR_DB}")
    print("\nNow run:  streamlit run app.py")


if __name__ == "__main__":
    main()
