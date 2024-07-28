from app import mongo

class Flight:
    @staticmethod
    def get_all_flights():
        return list(mongo.db.flights.find())

    @staticmethod
    def get_flight_by_id(flight_id):
        return mongo.db.flights.find_one({"_id": flight_id})

    @staticmethod
    def update_flight(flight_id, data):
        return mongo.db.flights.update_one({"_id": flight_id}, {"$set": data})

class User:
    @staticmethod
    def get_user_notifications(user_id):
        return mongo.db.users.find_one({"_id": user_id}, {"notifications": 1})

    @staticmethod
    def update_user_notifications(user_id, notifications):
        return mongo.db.users.update_one({"_id": user_id}, {"$set": {"notifications": notifications}})
