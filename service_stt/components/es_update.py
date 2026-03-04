from elasticsearch import Elasticsearch


class EsUpdate:
    def __init__(self,es_host,index,logger):
        self.es_host = es_host
        self.index =index
        self.logger = logger
        self.es = Elasticsearch(es_host)

    def update(self,extracted_info,file_id):
        self.es.update(index=self.index,id=file_id,doc=extracted_info)



# text = {'extracted_info':'welcome back today I cant stop thinking about Gaza the'}
# image_id = 'd3921482-fb8e-4c93-b253-fbc1a73fb212'
#
#
# es = EsUpdate('http://localhost:9200','metadata','aaa')
# es.update(text,image_id)