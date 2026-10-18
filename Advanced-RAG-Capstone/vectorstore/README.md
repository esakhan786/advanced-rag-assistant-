# vectorstore/

This folder holds the search index. It is created for you when you build the index,
and everything in it is git-ignored because it can always be rebuilt.

After running `python scripts/build_index.py` (or clicking **Build Vector DB** in the
app) you will find:

```text
vectorstore/
├── faiss/
│   ├── index.faiss     the embedding vectors, searched by meaning
│   └── index.pkl       the chunk texts and metadata that belong to those vectors
└── doc_store.json      every parent and child chunk, in plain JSON
```

**Why is `doc_store.json` separate from the vector index?**
Two parts of the pipeline do not use embeddings at all:

- **BM25 keyword search** needs the raw chunk text.
- **Parent recovery** needs to look up a parent chunk by its `parent_id`.

Keeping the chunks in a readable JSON file makes both trivial, and it is worth opening
the file once to see exactly what a "chunk" looks like.

When `VECTOR_DB=pinecone`, the vectors live in Pinecone instead of `faiss/`, but
`doc_store.json` is still written here for the two jobs above.
