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

class VectorStore:
    """
    Initiating Vector store
    """
    def __init__(self,emdmodel,dataSplits,embeddingModel):
        self.dataSplits = dataSplits
        self.embeddingModel = embeddingModel
        self.emdmodel = emdmodel

    def DocEmbedder(self):
        local_embeddings = OllamaEmbeddings(model=self.emdmodel)
        VecotorStore = Chroma.from_documents(
            documents=self.dataSplits,
            embedding=local_embeddings
        )
        return VecotorStore
