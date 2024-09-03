"""Mongo basics"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a document and returns its id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
