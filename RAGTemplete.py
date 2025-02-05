from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
class RAGTemplete:
    """
    RAGTemplete
    """
    def __init__(self, rag_template, format_docs, model,question,vectorstore):
        self.rag_template = rag_template
        self.format_docs = format_docs
        self.model = model
        self.question = question
        self.vectorstore = vectorstore

    def RagPrompt(self):
        ragprompt =  ChatPromptTemplate.from_template(self.rag_template)
        chain = (
            RunnablePassthrough.assign(context=lambda input: self.format_docs(input["context"]))
            | self.rag_prompt
            | self.model
            | StrOutputParser()
        )
        docs = self.vectorstore.similarity_search(self.question)
        chain.invoke({"context": docs, "question": self.question})
        return self.vectorstore.as_retriever()

