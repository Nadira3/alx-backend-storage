#!/usr/bin/env python3

""" module containing database function """


def list_all(mongo_collection):
    """
        function that lists all documents in a collection
    """
    return mongo_collection.find()
