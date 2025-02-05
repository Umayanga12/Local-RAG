from Logger import LoggerConfig, Logger

# Example usage
if __name__ == "__main__":
    config = LoggerConfig('Logs/app.log', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    config.configure()

    logger = Logger('app.log')
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.error('This is an error message')
    logger.warning('This is a warning message')
    logger.critical('This is a critical message')


RAG_TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that related information is not available. Use three sentences maximum and keep the answer concise.

<context>
{context}
</context>

Answer the following question:

{question}
"""

