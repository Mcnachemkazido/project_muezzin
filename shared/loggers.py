import logging
from elasticsearch import Elasticsearch
from datetime import datetime
from shared.loggers_variables import LoggersVariables


class Logger:
    _logger = None
    @classmethod
    def get_logger(cls, name=LoggersVariables.get_logger_name(),
                   es_host=LoggersVariables.get_es_uri(),
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
            logger.addHandler(logging.StreamHandler())
            logger.addHandler(ESHandler())
        cls._logger = logger
        return logger






