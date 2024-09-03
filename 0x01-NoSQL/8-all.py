#!/usr/bin/env python3
"""Mongodb basics"""


def list_all(mongo_collection):
    """Lists all documents in collection"""
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
