"""Mongo basics"""


def schools_by_topic(mongo_collection, topic):
    """Returns list of schools with certain topic"""
    docs = []
    docs = mongo_collection.find(
        {
            "topics": {
                "$in": topic
                }
        }
    )
