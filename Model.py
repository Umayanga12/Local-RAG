from langchain_ollama import ChatOllama

class model:
    """
    initiate  the model instance
    """
    def __init__(self,model):
        self.model = model

    def InitModel(self):
        model = ChatOllama(
            model=self.model
        )
        return model
