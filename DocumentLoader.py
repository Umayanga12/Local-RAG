import re

class ResourceType:
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
    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, 'r') as file:
            return file.read()
