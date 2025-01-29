import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('RAG')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler(log_file)
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def debug(self, message):
        self.logger.info(message)

    def info(self, message):
        self.logger.error(message)

    def error(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def critical(self, message):
        self.logger.critical(message)
