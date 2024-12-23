import logging
import threading


class Singleton(type):
    _instances = {}
    # Thread safety.
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            print('<Singleton> in the _call_...')
            if cls not in cls._instances:
                cls._instances[cls] = super(). \
                    __call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self):
        print('<Logger init> initializaing logger...')

        # Define the log message format
        formatter = logging \
            .Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create a logger object with the specified name
        self._logger = logging.getLogger('logger')
        self._logger.setLevel(logging.DEBUG)

        # Create a file handler to log messages to a file
        file_handler = logging.FileHandler('my_log_file.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Create a console handler to log messages to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger.
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)


def main():
    logger = Logger()
    # Only allow instantiate once.
    # logger2 = Logger()
    # print(logger == logger2) -> True
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')


if __name__ == '__main__':
    main()
