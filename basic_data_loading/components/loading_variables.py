import os
from dotenv import load_dotenv
load_dotenv()

class LoadingVariables:
    @staticmethod
    def get_path_files():
        path_files = os.getenv("PATH_FILES")
        if path_files:
            return path_files
        return False

    @staticmethod
    def get_kafka_host():
        kafka_host = os.getenv("BOOTSTRAP_SERVERS")
        if kafka_host:
            return kafka_host
        return False






