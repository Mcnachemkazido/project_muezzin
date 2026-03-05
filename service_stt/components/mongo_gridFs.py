from pymongo import MongoClient
import gridfs
import io


class MongoGridFs:
    def __init__(self,mongo_uri,db_name,logger):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)
        self.logger = logger
        self.logger.info('💚💚I successfully connected to mongodb.')



    def download_file(self,file_id):

        file_data = self.fs.find_one({'file_id':file_id})
        if file_data:

            self.logger.info(f'2️⃣i download new file from mongodb_grid_fs file id : {file_id}')
            return io.BytesIO(file_data.read())

        else:
            self.logger.error(f'2️⃣ error from download file mongodb_grid_fs')
            return False






