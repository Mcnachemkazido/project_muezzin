from confluent_kafka import Consumer
import json


class KafkaConsumer:
    def __init__(self,bootstrap_servers,group_id,topic_name,logger):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topic_name = topic_name
        self.logger = logger

        self.consumer_config = \
            {"group.id":self.group_id,
            "bootstrap.servers":self.bootstrap_servers,
            "auto.offset.reset": "earliest"}

        self.consumer = Consumer(self.consumer_config)
        self.consumer.subscribe([topic_name])

    def consume(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                self.logger.errer(f'error: {msg.error()}')
                continue

            info = json.loads(msg.value().decode('utf-8'))
            return info




# kafka_consumer = KafkaConsumer('localhost:9092','group_stt','stt','a')
# print(kafka_consumer.consume())