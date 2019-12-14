import pymongo
import json
from bson.code import Code
from bson.son import SON
import os
import csv

# myclient = pymongo.MongoClient("mongodb://76.67.179.162:27017/")

myclient = pymongo.MongoClient("mongodb://192.168.2.14:27017/")

mydb = myclient["hadoop"]

training = mydb["training"]
testing = mydb["testing"]
wordCount = mydb["wordCount"]


def populateTraining():
    input_file = csv.DictReader(open('NDBench-training.csv'))
    count = 0
    for row in input_file:
        
        json = {
            "key":count,
            "values": row
        }
        count += 1
        print(json)
        training.insert_one(json)

def populateTesting():
    input_file = csv.DictReader(open('NDBench-testing.csv'))
    for row in input_file:
        testing.insert_one(row)

lines = open('sampleWord.txt').readlines()
[wordCount.insert({'text':line}) for line in lines]

mapf = Code(open('wordMap.js', 'r').read())
reducef = Code(open('wordReduce.js', 'r').read())

results = wordCount.map_reduce(mapf, reducef, "out")

for result in results.find():
    print (result['_id'] , result['value']['count'])


# mapf = Code('''
# function(){
#         emit(self.key, self.values.NetworkIn_Average);
#     };
# }''')

# redecef = Code('''
# function(key, values){
#     var count = 0;
#     values.forEach(function(item){
#         count+=1;
#         });
#         return count;
# }''')

# finalisef = Code('''
# function(key, value){
#     return value;
# }
# ''')

# result = training.map_reduce(mapf, redecef, "myresult")
# for doc in result.find():
#     print(doc)