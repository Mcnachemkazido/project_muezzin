from elasticsearch import Elasticsearch


class EsIndex:
    def __init__(self,es_uri, index_name,logger):
        self.es_uri = es_uri
        self.index_name = index_name
        self.logger = logger

        self.es = Elasticsearch(self.es_uri)
        if not self.es.indices.exists(index=index_name):
            self.create_index()
            print('i create the index')
        else:
            print('the index already exists')


    def create_index(self):
        mapping =  {'properties':
            {
                'id': {'type': 'keyword'},
                'name': {'type': 'keyword'},
                'size_bytes': {'type': 'integer'},
                'modify_time': {'type': 'date'},
                'create_time': {'type': 'date'}
            }
                    }

        self.es.indices.create(index=self.index_name, mappings=mapping)


    def insert_new_value(self,value,file_id):
        self.es.index(index=self.index_name,id=file_id,document=value)
        self.logger.info(f'2️⃣i insert new value to mongodb file id:{file_id}')




