
class RiskAnalysis:
    def __init__(self,risk_lists:dict[str,list[str]],logger):
        self.risk_lists = risk_lists
        self.logger = logger


    def percentage_calculation(self,text:str):
        calculation = {'low_risk_hit': 0, 'high_risk_hit': 0,
                       'total_words': len(text.split())}

        for key, value in self.risk_lists.items():
            for item in value:
                if item in text:
                    if key == 'low_risk_decoded':
                        calculation['low_risk_hit'] += len(item.split())
                    else:
                        calculation['high_risk_hit'] += len(item.split()) * 2

        return ((calculation['low_risk_hit'] + calculation['high_risk_hit'])
                / calculation['total_words']) * 100


    @staticmethod
    def is_the_event_bad(percentage):
        if percentage <= 5:
            return False
        return True

    @staticmethod
    def danger_levels(percentage):
        if percentage <= 5:
            return 'none'
        elif percentage <= 10:
            return 'medium'
        else:
            return 'high'

    def analysis_summary(self,text):
        self.logger.info('2️⃣I did a risk analysis on the text.')
        percentage = self.percentage_calculation(text)
        return {'bds_percent': percentage,
                'is_bds': self.is_the_event_bad(percentage),
                'bds_threat_level': self.danger_levels(percentage)}



