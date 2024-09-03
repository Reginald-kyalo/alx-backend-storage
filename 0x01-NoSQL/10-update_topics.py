"""Mongo basics"""


def update_topics(mongo_collection, name, topics):
    """Updates document that matches certain field value"""
    mongo_collection.update(
        {
            name: name
        }, {
            '$set': {
                topics: [topics]
                }
            }
    )
