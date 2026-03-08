from elasticsearch import Elasticsearch


class EsConn:
    def __init__(self,es_uri):
        self.es_uri = es_uri
        self.es = Elasticsearch(self.es_uri)

    def ping(self):
        return f'the server is available: {self.es.ping()}'




