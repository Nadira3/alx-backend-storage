#!/usr/bin/env python3

""" module containing database function """


def insert_school(mongo_collection, **kwargs):
    """ function that inserts a new document in collection based on kwargs """
    return mongo_collection.insert_one(kwargs).inserted_id
