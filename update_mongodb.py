# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:21:07 2021

@author: prava
"""
import pymongo
client= pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb=client['Employee']
inventory=mydb.inventory

inventory.insert_many([
    {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}])

# Updating Record
# update record where item is sketch pad, set the size.uom to be 'm'
# and status to be 'p' and name a new field called lastModified and
# set also add currentDate as lastModified using $currentDate operator
inventory.update_one(
    {'item':'sketch pad'},
    {'$set':{'size.uom':'m', 'status':'P'},
     '$currentDate': {'lastModified':True}})
# Update many at once
inventory.update_many(
   {'qty':{'$lt':50}},
   {'$set': {'size.uom':'in', 'status':'p'},
    '$currentDate':{'lastModified':True}}
    )

# Replace the record with another record
inventory.replace_one(
    {'item':'paper'},
    {'item':'paper',
     'instock':[
         {'Warehouse':'A', 'qty':50},
         {'Warehouse':'C', 'qty':20}
         ]
     })
# replaced record with item paper as paper and added a 
# new field called instock and gave array as a value
# this array has 2 documents for dw A ad C

inventory.delete_one({'item':'paper','size.h':8.5})

'''
Delete operations remove documents from a collection. 
MongoDB provides the following methods to delete documents of a collection:

db.collection.deleteOne() New in version 3.2
db.collection.deleteMany() New in version 3.2

'''