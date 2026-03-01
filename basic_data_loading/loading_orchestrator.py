from components.loading_variables import LoadingVariables
from components.creating_metadata import CreatingMetadata
from components.kafka_producer import KafkaProducer
import os
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)






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


creating_metadata = CreatingMetadata(logging.getLogger(CreatingMetadata.__module__))

producer = KafkaProducer(LoadingVariables.get_kafka_host(),'basic_data',
                         logging.getLogger(KafkaProducer.__module__))

loading_orchestrator = LoadingOrchestrator(producer,creating_metadata,
                        LoadingVariables.get_path_files(),logger)



