import os
from components.loading_variables import LoadingVariables
from components.extract_metadata import ExtractMetadata
from components.kafka_producer import KafkaProducer

from shared.loggers import Logger
logger = Logger.get_logger()


class LoadingOrchestrator:
    def __init__(self,producer,create_metadata,path_files,logger):
        self.producer = producer
        self.create_metadata =create_metadata
        self.path_files = path_files
        self.logger = logger

    def run(self):
        self.logger.info('🤗🤗🤗 I started running the main loop that'
                         ' extracts metadata and sends to kafka')
        for file in os.scandir(self.path_files):
            info = {'meta_data': self.create_metadata.get_metadate(file),
                    'file_path': file.path}

            self.producer.send(info)


creating_metadata = ExtractMetadata(logger)

producer = KafkaProducer(LoadingVariables.get_kafka_host(),'basic_data',logger)


loading_orchestrator = LoadingOrchestrator(producer,creating_metadata,
                        LoadingVariables.get_path_files(),logger)



