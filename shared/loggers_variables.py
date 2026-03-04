import os
from dotenv import load_dotenv
load_dotenv()


class LoggersVariables:
    @staticmethod
    def get_es_uri():
        es_uri = os.getenv("ES_URI")
        if es_uri:
            return es_uri
        return False

    @staticmethod
    def get_logger_name():
        logger_name = os.getenv("LOGGER_NAME")
        if logger_name:
            return logger_name
        return False


