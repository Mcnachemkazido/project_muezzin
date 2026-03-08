from confluent_kafka import Producer
import json


class KafkaProducer:
    def __init__(self,bootstrap_servers,topic_name,logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic_name = topic_name
        self.logger = logger

        self.producer_config = {'bootstrap.servers':self.bootstrap_servers}
        self.producer = Producer(self.producer_config)


    def send(self,event: dict[str,str]):
        value = json.dumps(event).encode('utf-8')
        self.logger.info(f'5️⃣i send new msg to topic {self.topic_name}')
        self.producer.produce(topic=self.topic_name,value=value,callback=self.callback)
        self.producer.flush()



    def callback(self,err,msg):
        if err:
            self.logger.error(f'err: {err}')
        else:
            self.logger.info(msg.value())
            self.logger.info(f'topic: {msg.topic()}, offset: {msg.offset()}')

