from datetime import datetime


class CreatingMetadata:
    def __init__(self,logger):
        self.logger = logger

    def get_metadate(self,path):
        size_bytes = path.stat().st_size

        timestamp = path.stat().st_mtime
        modify_time = datetime.fromtimestamp(timestamp)

        current_timestamp = path.stat().st_ctime
        create_time = datetime.fromtimestamp(current_timestamp)

        self.logger.info(f'1️⃣I created metadata for file name: {path.name}')
        return {'name':path.name,'size_bytes':size_bytes,
                'modify_time':str(modify_time),'create_time':str(create_time)}

