#!/usr/bin/env python3

""" module containing database function """


def update_topics(mongo_collection, name, topics):
    """
        function that changes all topics of a school document
        based on the name
    """
    # Update all documents with the given name by setting the topics
    mongo_collection.update_many(
        {"name": name},              # Filter documents where name matches
        {"$set": {"topics": topics}}  # Update operation to set topics
    )
