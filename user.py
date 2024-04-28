class User:
    def __init__(self, username):
        self.username = username
        self.llm = "gemini-pro"
        self.embedder = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"