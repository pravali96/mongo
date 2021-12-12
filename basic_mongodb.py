# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:21:56 2021

@author: pravali
"""
import pymongo
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#Creating db
mydb=client['Employee'] #creates an instance of mydb called Employee

#check whether this db in created in mongodb compass

#Create a collection called employeeinformation in the database employee
information=mydb.employeeinformation

#Add a record 
record= {
     'firstname':'Teddy','lastname':'Bear', 
     'Department': "toy"
     }
information.insert_one(record)

# Insert multiple records

records = [{
    'firstname':'Mickey','lastname':'Mouse', 
     'Department': "char"
    },
    {
     'firstname':'Tom','lastname':'Jerry', 
     'Department': "show"
     },
    {
     'firstname':'Donald','lastname':'Duck', 
     'Department': "char"
     }]
information.insert_many(records)

information.find_one() # gives top one record

information.find() #returns a cursor that points to first record

for record in information.find():
    print(record)

# Query the json docs based on equality conditions
#select * from information where fname='sita'

information.find({'firstname':'Donald'}) #returns a cursor

for record in information.find({'Department':'char'}):
    print(record)
    
# Query docs using query operators- $in, $lt, $gt
for record in information.find({'Department':{'$in':['char', 'toy']}}):
    print(record)
    
# Using AND operation, query operator $lt is less than
for record in information.find({'Department':'toy', 'firstname':{'$lt':['teddy']}}):
    print(record)

#OR operator
for record in information.find({'$or':[{'firstname':'Teddy'}, {'Department':'char'}]}):
    print(record)
    
for record in information.find({'$and':[{'firstname':'Teddy'}, {'Department':'char'}]}):
    print(record)
    
inventory=mydb.inventory

inventory.insert_many( [
   { 'item': "journal", 'qty': 25, 'size': { 'h': 14, 'w': 21,'uom': "cm" }, 'status': "A" },
   { 'item': "notebook", 'qty': 50,'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "A" },
   { 'item': "paper", 'qty': 100, 'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "D" },
   { 'item': "planner", 'qty': 75, 'size': { 'h': 22.85,'w': 30,'uom': "cm" },'status': "D" },
   { 'item': "postcard", 'qty': 45, 'size': { 'h': 10, 'w': 15.25,'uom': "cm" },'status': "A" }
]); # Nested json for size

for record in inventory.find({'size':{'h':14, 'w': 21,'uom': "cm" }}):
    print(record)