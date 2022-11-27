import pymongo

class MongoAPI:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://mongodb:27017")
        self.DB = self.client['PosterDB']
    
    def CreateCollection(self,collectionName):
        self.mycoll = self.DB[collectionName]
        return self.mycoll
    
    def insertToCollection(self,dictionary):
        self.instertedValue = self.mycoll.insert_one(dictionary)
        return self.instertedValue
    
    def findInCollection(self,query=None):
        self.queryResult= self.mycoll.find(query)
        for i in self.queryResult:
            print(i)
    
    def deleteDocument(self,query):
        self.deletedQuery = self.mycoll.delete_many(query)
        return self.deletedQuery
    