from api.components.es_dal import EsDal
from api.components.es_conn import EsConn
from api.components.api_variables import ApiVariables
from api.components.moduls import FreeTextSearch

from shared.loggers import Logger
from fastapi import APIRouter
logger = Logger.get_logger()




es_conn = EsConn(ApiVariables.get_es_uri()).es
es_dal = EsDal(es_conn,'metadata')
route = APIRouter()
logger.info('🤗🤗🤗I put the server online.')


@route.get('/vents_by_bds_threat_level',tags=['level'])
def vents_by_bds_threat_level(level: str):
    logger.info('i return data form endpoint 1')
    return es_dal.events_by_bds_threat_level(level)


@route.get('/all_events_found_problematic',tags=['all_events'])
def all_events_found_problematic(display_text:bool):
    logger.info('i return data form endpoint 2')
    return es_dal.all_events_found_problematic(display_text)


@route.get('/get_aggregation_percent',tags=['agg'])
def get_aggregation_percent(kind:str):
    logger.info('i return data form endpoint 3')
    return es_dal.get_aggregation_percent(kind)


@route.post('/free_text_search',tags=['free_text'])
def free_text_search(text: FreeTextSearch):
    logger.info('i return data form endpoint 4')
    return es_dal.free_text_search(text.operator,text.search)


@route.get('/number_events_each_level')
def number_events_each_level():
    logger.info('i return data form endpoint 5')
    return es_dal.number_events_each_level()

@route.get('/average_risk_percentage_for_each_level')
def average_risk_percentage_for_each_level():
    logger.info('i return data form endpoint 6')
    return es_dal.average_risk_percentage_for_each_level()