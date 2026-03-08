from components.kafka_consumer import KafkaConsumer
from components.mongo_gridFs import MongoGridFs
from components.stt import Stt
from components.es_update import EsUpdate
from components.stt_variables import SttVariables
from components.kafka_producer import KafkaProducer

from shared.loggers import Logger
logger = Logger.get_logger()



class SttOrchestrator:
    def __init__(self,consumer:KafkaConsumer,mongo_grid_fs:MongoGridFs,
                 stt:Stt,es_update:EsUpdate,producer:KafkaProducer,logger):
        self.consumer = consumer
        self.mongo_grid_fs = mongo_grid_fs
        self.stt = stt
        self.es_update = es_update
        self.producer = producer
        self.logger = logger

    def run(self):
        self.logger.info('😌😛😜I started running the main loop that extracts text from an audio file.')
        while True:
            file_id = self.consumer.consume()
            file_object = self.mongo_grid_fs.download_file(file_id)
            file_stt = self.stt.conversion_to_text(file_object)
            self.es_update.update(file_stt,file_id)
            self.producer.send({'file_id':file_id,'file_sst':file_stt})



kafka_consumer = KafkaConsumer(SttVariables.get_kafka_host(),'sst_group','stt',logger)
stt = Stt(logger)
conn_mongo = MongoGridFs(SttVariables.get_mongo_uri(),'muezzin',logger)
conn_es = EsUpdate(SttVariables.get_es_uri(),'metadata',logger)
kafka_producer = KafkaProducer(SttVariables.get_kafka_host(),'analysis',logger)

stt_orchestrator = SttOrchestrator(kafka_consumer,conn_mongo,stt,conn_es,kafka_producer,logger)



