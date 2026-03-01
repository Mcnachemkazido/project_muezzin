from confluent_kafka import Consumer
import json
from uuid import uuid4

from storage_variables import StorageVariables
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




class KafkaConsumer:
    def __init__(self,group_id,topic_name,bootstrap_servers,logger):
        self.topic_name = topic_name
        self.bootstrap_servers = bootstrap_servers
        self.logger = logger
        self.group_id = group_id

        self.consumer_config = {'bootstrap.servers':self.bootstrap_servers,
                                'group.id':self.group_id,
                                "auto.offset.reset": "earliest"}

        self.consumer = Consumer(self.consumer_config)
        self.consumer.subscribe([self.topic_name])


    def consume(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    self.logger.error(f'error: {msg.error()}')

                data = json.loads(msg.value().decode('utf-8'))
                data['id'] = str(uuid4())
                return data
        except KeyboardInterrupt:
            self.logger.info("Stopping consumer")
        finally:
            self.consumer.close()


c = KafkaConsumer('storage_group','basic_data',StorageVariables.get_kafka_host(),logger)
print(c.consume())
