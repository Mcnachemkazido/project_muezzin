import os
from dotenv import load_dotenv
load_dotenv()

class SttVariables:

    @staticmethod
    def get_kafka_host():
        kafka_host = os.getenv("BOOTSTRAP_SERVERS")
        if kafka_host:
            return kafka_host
        return False

    @staticmethod
    def get_es_uri():
        es_uri = os.getenv("ES_URI")
        if es_uri:
            return es_uri
        return False

    @staticmethod
    def get_mongo_uri():
        mongo_uri = os.getenv("MONGO_URI")
        if mongo_uri:
            return mongo_uri
        return False







