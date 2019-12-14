import pymongo
import json
from bson.code import Code
from bson.son import SON
import os
import csv


def uploadData(dataset, attribute):
    input_file = csv.DictReader(open(dataset))
    for row in input_file:
        # print(row[attribute])S
        col.insert_one(row)


# myclient = pymongo.MongoClient("mongodb://76.67.179.162:27017/")
myclient = pymongo.MongoClient("mongodb://192.168.2.14:27017/")
mydb = myclient["hadoop"]


col = mydb["MapRedData"]
# col.drop()

# print('Uploading Selected Data to MongoDB')
# uploadData('NDBench-testing.csv', 'Final_Target')
# print('Upload Completed Successfully')


mapf = Code(open('mapFinal.js', 'r').read())
reduceMin = Code(open('reduceMin.js', 'r').read())
reduceMax = Code(open('reduceMax.js', 'r').read())

out = mydb["out"]
results = col.map_reduce(mapf, reduceMin,'out')
results = col.map_reduce(mapf, reduceMax, 'out')

for result in results.find():
    print(result['_id'])