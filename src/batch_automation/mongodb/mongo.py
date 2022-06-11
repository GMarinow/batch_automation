from pprint import pprint
import pymongo

def InsertDocument(collection, **kwargs):
    collection.insert_one(kwargs)
    pprint (kwargs)

def InsertDocumentDict(collection, dict):
    collection.insert_one(dict)
    pprint (dict)

def DeletellDocuments(collection):
    return collection.delete_many({})

def DropCollection(collection):
    return collection.drop({})

def CountAllDocuments(collection):
    return collection.count_documents({})

def GetAllDocuments(collection):
    all_documents = []
    documents = collection.find({})
    for document in documents:
        all_documents.append(document)
    return all_documents

def FindDocuments(collection, **kwargs):
    all_documents = []
    for kwargsKeys, kwargsValues in kwargs.items():
        documents = collection.find({kwargsKeys: {"$regex": kwargsValues}})
        for document in  documents:
            all_documents.append(document)
    return (all_documents)

def FindDocument(collection, **kwargs):
    for kwargsKeys, kwargsValues in kwargs.items():
        documents = collection.find({kwargsKeys: {"$regex": kwargsValues}})
        for items in  documents:
            return items[kwargsKeys]

def FindValue(collection, value):
    all_documents = []
    for documents in GetAllDocuments(collection):
        for k, v in documents.items():
            if value == k:
                all_documents.append(v)
    return all_documents