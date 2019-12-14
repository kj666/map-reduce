import pymongo
import json
from bson.code import Code
from bson.son import SON
import os
import csv

# myclient = pymongo.MongoClient("mongodb://76.67.179.162:27017/")

myclient = pymongo.MongoClient("mongodb://192.168.2.14:27017/")

mydb = myclient["hadoop"]

wordCount = mydb["wordCount"]

lines = open('sampleWord.txt').readlines()
[wordCount.insert({'text':line}) for line in lines]

mapf = Code(open('wordMap.js', 'r').read())
reducef = Code(open('wordReduce.js', 'r').read())

results = wordCount.map_reduce(mapf, reducef, "out")

for result in results.find():
    print (result['_id'] , result['value']['count'])
