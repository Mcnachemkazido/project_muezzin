import os
from dotenv import load_dotenv
load_dotenv()

class ApiVariables:

    @staticmethod
    def get_es_uri():
        kafka_host = os.getenv("ES_URI")
        if kafka_host:
            return kafka_host
        return False








