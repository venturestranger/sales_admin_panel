import pymongo
from utils import Ad
from config import Config


connection = pymongo.MongoClient(Config.MONGO_URI)
db = connection[Config.MONGO_DATABASE]
collection = db[Config.MONGO_COLLECTION]

ads = [Ad(1, 'hello world', '1971-02-11', '70000', '+777777777'), Ad(0, 'hello world', '1871-12-11', '90000', '+777777777')]

def retrieve() -> list:
	docs = collection.find({'active': True})
	ret = []

	for doc in docs:
		ret.append(Ad(doc['_id'], doc['content'], str(doc['date']), doc['cost'], doc['contact']))
	
	return ret


def disable(id): 
	collection.update_one({'_id': id}, {'$set': {'active': False}})
