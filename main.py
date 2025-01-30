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
