import pymongo
import gridfs

class MongoAPI:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.DB = self.client['PosterDB']
        self.mycoll = self.DB['Images']
        self.fs = gridfs.GridFS(self.DB)
    
    # def CreateCollection(self,collectionName):
    #     self.mycoll = self.DB[collectionName]
    #     return self.mycoll
    
    # def insertToCollection(self,dictionary):
    #     instertedValue = self.mycoll.insert_one(dictionary)
    #     return instertedValue
    
    # def findInCollection(self,query=None):
    #     queryResult= self.mycoll.find(query)
    #     for i in queryResult:
    #         print(i)
    
    # def deleteDocument(self,query):
    #     deletedQuery = self.mycoll.delete_many(query)
    #     return deletedQuery
    
    def uploadImage(self,data,filename1):
        self.fs.put(data,filename=filename1)
