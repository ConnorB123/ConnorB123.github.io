import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 51917)
class auctionbid(object):
    """ CRUD operations for Auction in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:51917/?authMechanism=DEFAULT&authSource=BID' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:51917')
        self.database = self.client['BID']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary 
            if insert != 0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")


# Create method to implement the R in CRUD.
    def create(self, data):
        if data is not None:
            return self.database.animals.find_one(data) 
        else:
                print('Nothing to read, because data parameter is empty')
                return False 

    