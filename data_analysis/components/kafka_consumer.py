from confluent_kafka import Consumer
import json

class KafkaConsumer:
    def __init__(self,bootstrap_servers,group_id,topic_name,logger):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topic_name = topic_name
        self.logger = logger

        self.consumer_config  = \
            {'bootstrap.servers':self.bootstrap_servers,
            'group.id':self.group_id,
            "auto.offset.reset": "earliest"}
        self.consumer = Consumer(self.consumer_config)
        self.consumer.subscribe([topic_name])

    def consume(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                self.logger.error(f'error: {msg.error()}')
                continue

            value = json.loads(msg.value().decode('utf-8'))
            self.logger.info(f'1️⃣i consume new data from topic: {self.topic_name}')
            return value


