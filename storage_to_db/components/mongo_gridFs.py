from pymongo import MongoClient
import gridfs


class MongoGridFs:
    def __init__(self,mongo_uri,db_name,logger):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)
        self.logger = logger


    def storing_in_grid_fs(self,file_path,file_id):
        with open(file_path, 'rb') as file_data:
            self.fs.put(file_data,file_id=file_id, description='metadata from sound')
            self.logger.info(f"3️⃣i insert new value to mongodb file id: {file_id}")


