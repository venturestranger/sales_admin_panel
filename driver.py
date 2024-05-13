import pymongo
from utils import Ad
from config import Config


connection = pymongo.MongoClient(Config.MONGO_URI)
db = connection[Config.MONGO_DATABASE]
collection = db[Config.MONGO_COLLECTION]


def retrieve() -> list:
	docs = collection.find({'active': True})
	ret = []

	for doc in docs:
		ret.append(Ad(doc['_id'], doc['name'], doc['content'], str(doc['date']), doc['cost'], doc['contact']))
	
	return ret


def disable(id): 
	collection.update_one({'_id': id}, {'$set': {'active': False}})
