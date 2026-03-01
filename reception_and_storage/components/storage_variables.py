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


