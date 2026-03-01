from confluent_kafka import Producer
import json


class KafkaProducer:
    def __init__(self,bootstrap_servers,topic_name,logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic_name = topic_name
        self.logger = logger

        self.producer_config = {'bootstrap.servers':self.bootstrap_servers}
        self.producer = Producer(self.producer_config)


    def send(self,event):
        value = json.dumps(event).encode('utf-8')
        self.producer.produce(topic=self.topic_name,value=value,callback=self.callback)
        self.logger.info(f'2️⃣ i send to kafka file file name: {event['meta_data']['name']}')
        self.producer.flush()


    def callback(self,err,msg):
        if err:
            self.logger.error(f'error: {err}')

        else:
            self.logger.info(f'msg: {msg.value().decode('utf-8')}')
            self.logger.info(f'topic: {msg.topic()}, offset: {msg.offset()}')
