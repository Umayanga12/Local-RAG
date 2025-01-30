from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

class TextSplitter:
    """
    Split the text into chunks
    """
    def __init__(self, chunk_size, chunk_overlap):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, data):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        all_splits = text_splitter.split_documents(data)
        return all_splits

class Embedder:
    def __init__(self,model,dataSplits,embeddingModel):
        pass

    def DocEmbedder(self):
        pass
