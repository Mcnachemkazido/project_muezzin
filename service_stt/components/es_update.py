from elasticsearch import Elasticsearch


class EsUpdate:
    def __init__(self,es_host,index,logger):
        self.es_host = es_host
        self.index =index
        self.logger = logger
        self.es = Elasticsearch(es_host)


    def update(self,extracted_info,file_id):
        self.es.update(index=self.index,id=file_id,doc={'extracted_info':extracted_info})
        self.logger.info(f'4️⃣I updated the index:{self.index} in es with new data fron file id {file_id}')



