import os
from dotenv import load_dotenv
load_dotenv()

class StorageVariables:

    @staticmethod
    def get_kafka_host():
        kafka_host = os.getenv("BOOTSTRAP_SERVERS")
        if kafka_host:
            return kafka_host
        return False

    @staticmethod
    def get_es_uri():
        kafka_host = os.getenv("ES_URI")
        if kafka_host:
            return kafka_host
        return False

    @staticmethod
    def get_mongodb_uri():
        mongodb_uri = os.getenv("MONGO_URI")
        if mongodb_uri:
            return mongodb_uri
        return False



    @staticmethod
    def get_logger_name():
        logger_name = os.getenv("LOGGER_NAME")
        if logger_name:
            return logger_name
        return False








