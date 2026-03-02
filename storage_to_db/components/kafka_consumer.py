from confluent_kafka import Consumer
import json
from uuid import uuid4


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
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                self.logger.error(f'error: {msg.error()}')

            data = json.loads(msg.value().decode('utf-8'))
            data['id'] = str(uuid4())
            self.logger.info(f'1️⃣I got a new message from topic {self.topic_name} \n'
                             f'and crate file id: {data["id"]}')
            return data

