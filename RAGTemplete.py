from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

class RAGTemplete:
    """
    RAGTemplete
    """
    def __init__(self, rag_template):
        self.rag_template = rag_template

    def RagPrompt(self):
        return ChatPromptTemplate.from_template(self.rag_template)
