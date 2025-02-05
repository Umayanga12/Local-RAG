from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class QnA:
    """
    QnA
    """
    def __init__(self, retriever, format_docs, model, question, rag_prompt):
        self.retriever = retriever
        self.format_docs = format_docs
        self.model = model
        self.question = question
        self.rag_prompt = rag_prompt

    def QnA(self):
        qa_chain = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | self.rag_prompt
            | self.model
            | StrOutputParser()
        )
        return qa_chain.invoke(self.question)