from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings

class MongoDBStorage:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client["tour_agency"]
        self.tours = self.db.get_collection(settings.TOURS_COLLECTION)

storage = MongoDBStorage()
