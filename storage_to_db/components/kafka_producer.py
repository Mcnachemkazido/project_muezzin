from confluent_kafka import Producer
import json


class KafkaProducer:
    def __init__(self,bootstrap_servers,topic_mame,logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic_name = topic_mame
        self.logger = logger

        self.producer_config = {"bootstrap.servers":self.bootstrap_servers}
        self.producer = Producer(self.producer_config)

    def run(self,event):
        value = json.dumps(event).encode('utf-8')
        self.logger.info(f'4️⃣I sent a file ID for further processing to topic :{self.topic_name}')
        self.producer.produce(topic=self.topic_name,value=value,callback=self.callback)
        self.producer.flush()

    def callback(self,err,msg):
        if err:
            self.logger.errer(f'err: {err}')
        if msg:
            self.logger.info(f"msg:{msg.value().decode('utf-8')}")
            self.logger.info(f'topic :{msg.topic()}, offset:{msg.offset()}')



