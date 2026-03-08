from components.analysis_variables import AnalysisVariables
from components.kafka_consumer import KafkaConsumer
from components.lists_decoding import ListsDecoding
from components.risk_analysis import RiskAnalysis
from components.es_update import EsUpdate
from shared.loggers import Logger
logger = Logger.get_logger()


class AnalysisOrchestrator:
    def __init__(self,consumer:KafkaConsumer,risk_calculation:RiskAnalysis,
                 es_update:EsUpdate,logger):
        self.consumer = consumer
        self.risk_calculation = risk_calculation
        self.es_update = es_update
        self.logger = logger

    def run(self):
        logger.info('🤓🤓🤓I started running the main loop that does'
                    ' calculations on the text and updates in es')
        while True:
            data = self.consumer.consume()
            risk_analysis_summary = self.risk_calculation.analysis_summary(data['file_sst'])
            self.es_update.update(data=risk_analysis_summary,id=data['file_id'])





kafka_consumer = KafkaConsumer(AnalysisVariables.get_kafka_host(),
                               'group_analysis','analysis',logger)
suspicious_lists = ListsDecoding(logger).decoding()
risk_analysis = RiskAnalysis(suspicious_lists,logger)
es = EsUpdate(AnalysisVariables.get_es_uri(),'metadata',logger)


analysis_orchestrator = AnalysisOrchestrator(kafka_consumer,risk_analysis,es,logger)
