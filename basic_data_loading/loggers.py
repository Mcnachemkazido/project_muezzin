import logging
from elasticsearch import Elasticsearch
from datetime import datetime
from components.loading_variables import LoadingVariables


class Logger:
    _logger = None
    @classmethod
    def get_logger(cls,name=LoadingVariables.get_logger_name(),
                   es_host=LoadingVariables.get_es_uri(),
                    index="logger", level=logging.DEBUG):
        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)
            class ESHandler(logging.Handler):
                def emit(self, record):
                     try:
                         es.index(index=index, document={
                         "timestamp": datetime.utcnow().isoformat(),
                        "level": record.levelname,
                        "logger": record.name,
                        "message": record.getMessage()
                         })
                     except Exception as e:
                        print(f"ES log failed: {e}")
            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())
        cls._logger = logger
        return logger


