import re
from Logger import  LoggerConfig,Logger
from langchain_community.document_loaders import WebBaseLoader

configDocLoadLogger = LoggerConfig('Logs/Doc_Loading/DocumentLoader.log', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
configDocLoadLogger.configure()

DocLoaderLogger = Logger('Logs/Doc_Loading/DocumentLoader.log')

class ResourceType:
    """
    Chech whether the given resource is a web based resource or a local file
    """
    def __init__(self, ResourcePath):
        self.resource = ResourcePath

    def isWebBased(self) -> bool:
        web_url_pattern = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return True if re.match(web_url_pattern, self.resource) else False


class DocumentLoader(ResourceType):
    """
    Load the document from the given resource
    """
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            if self.isWebBased():
                loader = WebBaseLoader(self.path)
                data = loader.load()
                return data
            else:
                with open(self.path, 'r') as file:
                    return file.read()
        except Exception as e:
            DocLoaderLogger.error(f"Error in loading the document: {e}")
            return None
