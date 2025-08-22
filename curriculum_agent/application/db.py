import os
import shutil
from langchain_openai import OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma
from langchain_core.documents import Document

class ChromaDB:

    CHROMA_PATH = "./db/"

    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.client = Chroma('curriculum', self.embeddings, persist_directory=self.CHROMA_PATH)

    def save(self, chunks: Document):
        """
        Salva a lista de chunks no ChromaDB
        """
        #if os.path.exists(self.CHROMA_PATH):
        #    shutil.rmtree(self.CHROMA_PATH)

        self.client.add_documents(chunks)

    def similarity_search_with_score(self, query: str, k: int = 3):
        results = self.client.similarity_search_with_score(query, k=k)
        return [(doc, score) for doc, score in results]