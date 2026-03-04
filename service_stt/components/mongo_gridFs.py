from pymongo import MongoClient
import gridfs
import io

class MongoGridFs:
    def __init__(self,mongo_uri,db_name,logger):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)
        self.logger = logger

    def download_file(self,file_id):
        file_data = self.fs.find_one({'file_id':file_id})
        if file_data:
            return io.BytesIO(file_data.read())

        else:
            return False



# image_id = 'd3921482-fb8e-4c93-b253-fbc1a73fb212'
# uri = 'mongodb://root:asdf@localhost:27017'
# name = 'muezzin'
# m = MongoGridFs(uri,name,'a')
# x = m.download_file(image_id)


