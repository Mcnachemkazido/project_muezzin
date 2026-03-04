from components.storage_variables import StorageVariables
from components.kafka_consumer import KafkaConsumer
from components.es_index import EsIndex
from components.mongo_gridFs import MongoGridFs
from components.kafka_producer import KafkaProducer


from shared.loggers import Logger
logger = Logger.get_logger()



class StorageOrchestrator:
    def __init__(self,consumer,es_index,mongo_gfs,producer,logger):
        self.consumer = consumer
        self.es_index = es_index
        self.mongo_gfs = mongo_gfs
        self.producer = producer
        self.logger = logger


    def run(self):
        self.logger.info('☺️☺️☺️ Starts running the main loop that maintains es and mongodb')
        while True:
            data = self.consumer.consume()
            file_id = data['id']
            self.es_index.insert_new_value(data['meta_data'],file_id)
            self.mongo_gfs.storing_in_grid_fs(data['file_path'],file_id)
            self.producer.run(file_id)



kafka_consumer = KafkaConsumer('storage_group','basic_data'
        ,StorageVariables.get_kafka_host(),logger)

es = EsIndex(StorageVariables.get_es_uri(),
             'metadata',logger)

mongo_grid_fs = MongoGridFs(StorageVariables.get_mongodb_uri(),
                      'muezzin',logger)

kafka_producer = KafkaProducer(StorageVariables.get_kafka_host(),'stt',logger)


storage_orchestrator = StorageOrchestrator(kafka_consumer,es,mongo_grid_fs,kafka_producer,logger)





