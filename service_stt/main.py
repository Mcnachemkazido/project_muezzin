from elasticsearch import Elasticsearch


es = Elasticsearch('http://localhost:9200')


res = es.search(index='metadata',query={'match_all':{}},size=100)
hits = res['hits']['hits']
for hit in hits:
    print(hit)