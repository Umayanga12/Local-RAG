from langchain_core.output_parsers import StrOutputParser

class ConvertDocsToText:
    """
    Convert the documents to text
    """
    def __init__(self, docs):
        self.docs = docs

    def format_docs(self):
        return "\n\n".join(doc.page_content for doc in self.docs)


class Chain(ConvertDocsToText):
    """
    Chain the documents to text
    """
    def __init__(self, docs, prompt, model,vectorstore):
        super().__init__(docs)
        self.prompt = prompt
        self.model = model
        self.vectorstore = vectorstore

    def chain(self):
        return {"docs": self.format_docs()} | self.prompt | self.model | StrOutputParser()

    def CheckForSimilarity(self):
        return self.vectorstore.similarity_search(self.question)