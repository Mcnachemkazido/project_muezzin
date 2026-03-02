from components.storage_variables import StorageVariables
from components.kafka_consumer import KafkaConsumer
from components.es_index import EsIndex
from components.mongo_gridFs import MongoGridFs

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StorageOrchestrator:
    def __init__(self,consumer,es_index,mongo_gfs,logger):
        self.consumer = consumer
        self.es_index = es_index
        self.mongo_gfs = mongo_gfs
        self.logger = logger


    def run(self):
        self.logger.info('☺️☺️☺️ Starts running the main loop that maintains es and mongodb')
        while True:
            data = self.consumer.consume()
            file_id = data['id']
            self.es_index.insert_new_value(data['meta_data'],file_id)
            self.mongo_gfs.storing_in_grid_fs(data['file_path'],file_id)



kafka_consumer = KafkaConsumer('storage_group','basic_data'
        ,StorageVariables.get_kafka_host(),logging.getLogger(KafkaConsumer.__module__))

es = EsIndex(StorageVariables.get_es_uri(),
             'metadata',logging.getLogger(EsIndex.__module__))

mongo_grid_fs = MongoGridFs(StorageVariables.get_mongodb_uri(),
                      'muezzin',logging.getLogger(MongoGridFs.__module__))



storage_orchestrator = StorageOrchestrator(kafka_consumer,es,mongo_grid_fs,logger)




