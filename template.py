from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class PromptTemplate:
    """
    Define the prompt template
    """
    def __init__(self, base_prompt):
        self.base_prompt = base_prompt

    def get_prompt(self):
        return ChatPromptTemplate.from_template(self.base_prompt)
