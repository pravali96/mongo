# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:53:43 2021

@author: prava
"""
'''
database as a service.This service is mongodb Atlas. It can be hosted on azure, aws or google cloud platforms.These are infrastructure as services.
These services provide infrastructure as needed. we can install the libraries as needed and move ahead. Then we have platform 
as a service where the infrastructure, installation part is also taken care of such as Heroku. We only pass requirement.txt.
 We can create clusters of dbs. cluster is nothing but a replica of data and based on traffic that request may go to different clusters
This is done for scalability. Team doesnt has to take care of configuration and maintenance of dbs on premises.

Login into atlas webiste, create a cluster,click on connect and copy the server url. 
Go to mongodb compass, click on connect to and paste the server url connection. This opens up the connection to the cluster
Then in the code, in MongoClient, copy this server url connection
password: 3131, username: pravali96

For server install pip install pymongo[srv]
'''
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:52:11 2021

@author: pravali
"""
# creation of object MongoClient

import pymongo
client=pymongo.MongoClient('mongodb+srv://pravali96:3131@mydb.elzxh.mongodb.net/test')

# Access Database
mydatabase=client['Students']

#Access Collection
collection=mydatabase['StudentScores']

# Inserting data
data = [ 
    {"user":"Krish", "subject":"Database", "score":80}, 
    {"user":"Amit",  "subject":"JavaScript", "score":90}, 
    {"user":"Amit",  "title":"Database", "score":85}, 
    {"user":"Krish",  "title":"JavaScript", "score":75}, 
    {"user":"Amit",  "title":"Data Science", "score":60},
    {"user":"Krish",  "title":"Data Science", "score":95}] 
  
collection.insert_many(data)

# Find total number of records taken by each user
# Perform aggregation using $group  based on $user
# _id is just like a name and we are summing the subjects
agg_results=collection.aggregate(
    [{
    '$group':
        {'_id':'$user',
        'Num_of_subjs':{'$sum':1}  
      }}
     ])
        
for i in agg_results:
    print(i)

#calculating total score for each user

aggr_2= collection.aggregate(
    [{
      '$group': {
          '_id':'$user',
          'total_score':{'$sum':'$score'}
          }
      }])
for i in aggr_2:
    print(i)

#calculating avg score for each user    
agg_3=collection.aggregate([
    {
     '$group':{
         '_id':'$user',
         'avg_score': {'$avg':'$score'}
         }
     }])
for i in agg_3:
    print(i)

import datetime as datetime

# Create a new collection
data=[{ "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : datetime.datetime.utcnow()},
{ "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : datetime.datetime.utcnow() },
{ "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 5, "date" : datetime.datetime.utcnow() },
{ "_id" : 4, "item" : "abc", "price" : 10, "quantity" : 10, "date" : datetime.datetime.utcnow() },
{ "_id" : 5, "item" : "xyz", "price" : 5, "quantity" : 10, "date" :datetime.datetime.utcnow() }]

mycollection=mydatabase['stores']
mycollection.insert_many(data)

# calculate avg qty, avg price
aggr_4=mycollection.aggregate([
    {'$group':
     { 
     '_id':'$item',
     'avg_qty':{'$avg':'$quantity'},
     'avg_price':{'$avg':{'$multiply':['$price','$quantity']}}      
     }
     }])
for i in aggr_4:
    print(i)

# Adding new data, _id is the unique id of the record in mongodb
data=[{
  "_id" : 1,
  "title": "abc123",
  "isbn": "0001122223334",
  "author": { "last": "zzz", "first": "aaa" },
  "copies": 5
},
{
  "_id" : 2,
  "title": "Baked Goods",
  "isbn": "9999999999999",
  "author": { "last": "xyz", "first": "abc", "middle": "" },
  "copies": 2
}
]

# Access collection of the database
col=mydatabase['Books']

col.insert_many(data)

#Project is same as select title, isbn from books
for row in col.aggregate([{'$project':{'title':1,'isbn':1}}]):
    print(row)