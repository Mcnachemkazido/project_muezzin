import base64
import json


class ListsDecoding:
    def __init__(self,logger):
        self.high_risk_original = None
        self.low_risk_original = None
        self.logger = logger
        self.read_risk_lists()




    def read_risk_lists(self):
        with open('data_analysis/data/lists.json') as file:
            data = json.load(file)
            self.high_risk_original = data['low_risk']
            self.low_risk_original = data['high_risk']
            self.logger.info('I was able to open and read the file.')


    def decoding(self):
        base64_bytes = self.high_risk_original.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        high_risk_decoded = sample_string_bytes.decode("ascii")

        base64_bytes = self.low_risk_original.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        low_risk_decoded = sample_string_bytes.decode("ascii")

        self.logger.info('I was able to open and read the file')
        return {"low_risk_decoded":low_risk_decoded.lower().split(','),
                "high_risk_decoded":high_risk_decoded.lower().split(',')
                }





