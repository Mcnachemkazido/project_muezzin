
class EsDal:
    def __init__(self,es_conn,index):
        self.es_conn = es_conn
        self.index = index

    def events_by_bds_threat_level(self,level:str):
        query = {'term':{'bds_threat_level':level}}
        source = ['create_time','bds_percent','bds_threat_level']

        res = self.es_conn.search(_source= source,query=query,size=50,index=self.index,)
        response = [hit['_source'] for hit in res['hits']['hits']]
        return response


    def all_events_found_problematic(self,display_text:bool):
        query = {'term': {'is_bds': True}}
        source = ['create_time', 'bds_percent', 'bds_threat_level']
        if display_text: source.append('extracted_info')
        res = self.es_conn.search(_source=source, query=query, size=50, index=self.index)
        response = [hit['_source'] for hit in res['hits']['hits']]
        return response


    def get_aggregation_percent(self,kind:str):
        query = {'match_all': {}}
        aggs = {'calculation': {kind: {'field': 'bds_percent'}}}

        res = self.es_conn.search(query=query, aggs=aggs, size=0, index='metadata')
        return res['aggregations']['calculation']['value']


    def free_text_search(self,operator: str,search: str):
        query = {'match': {'extracted_info': {'query':search, 'operator':operator}}}
        res = self.es_conn.search(query=query, size=50, index=self.index)
        response = [hit['_source'] for hit in res['hits']['hits']]
        return response


    def number_events_each_level(self):
        query = {'match_all': {}}
        aggs = {'my_buckets':
            {'terms': {
                'field': 'bds_threat_level'
            }}}

        res = self.es_conn.search(query=query, aggs=aggs, size=0, index=self.index)
        return res['aggregations']['my_buckets']['buckets']


    def average_risk_percentage_for_each_level(self):
        query = {'match_all': {}}

        aggs = {'my_agg':
                    {'terms':
                         {'field': 'bds_threat_level'},
                     'aggs':
                         {'avg':
                              {'avg':
                                   {'field': 'bds_percent'}
                               }
                          }
                     }
                }
        res = self.es_conn.search(query=query, aggs=aggs, size=0, index='metadata')
        response = [{i['key']: i['avg']['value']} for i in res['aggregations']['my_agg']['buckets']]
        return response






