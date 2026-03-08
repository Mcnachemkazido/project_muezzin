from elasticsearch import Elasticsearch

class EsUpdate:
    def __init__(self,es_host,index,logger):
        self.es_host = es_host
        self.index = index
        self.logger = logger

        self.es = Elasticsearch(self.es_host)

    def ping_to_es(self):
        return f'the es is available: {self.es.ping()}'

    def update(self,data,id):
        self.es.update(index=self.index,doc=data,id=id)
        self.logger.info(f'3️⃣I updated the data in es for id:{id}')



