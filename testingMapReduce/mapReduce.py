import pymongo
import json
from bson.code import Code
from bson.son import SON
import os
import csv


def uploadData(dataset, attribute, collection):
    collection.drop()
    input_file = csv.DictReader(open(dataset))
    line = 0
    for row in input_file:
        inline = {
            'CPUUtilization_Average': int(row['CPUUtilization_Average']),
            'NetworkIn_Average' : int(row['NetworkIn_Average']),
            'NetworkOut_Average' : int(row['NetworkOut_Average']),
            'MemoryUtilization_Average' : float(row['MemoryUtilization_Average']),
            'Final_Target' : float(row['Final_Target'])
        }
        # print (inline)
        col.insert_one(inline)


# myclient = pymongo.MongoClient("mongodb://76.67.179.162:27017/")
myclient = pymongo.MongoClient("mongodb://192.168.2.14:27017/")
mydb = myclient["hadoop"]


col = mydb["MapRedData"]

print('Uploading Selected Data to MongoDB')
uploadData('test.csv', 'Final_Target', col)
print('Upload Completed Successfully')


mapf = Code(open('mapCPU.js', 'r').read())
reduceMin = Code(open('reduceMin.js', 'r').read())
reduceMax = Code(open('reduceMax.js', 'r').read())
reduceMedian = Code(open('reduceMedian.js', 'r').read())
reduceAverage = Code(open('reduceAverage.js', 'r').read())
reduceStandard = Code(open('reduceStandardDeviation.js', 'r').read())
out = mydb["out"]


minValue = col.map_reduce(mapf, reduceMin,'out')
print('Min: ' + str(minValue.find()[0]['value']))

maxValue = col.map_reduce(mapf, reduceMax, 'out')
print('Max: ' + str(maxValue.find()[0]['value']))

medianValue = col.map_reduce(mapf, reduceMedian, 'out')
print('Median: ' + str(medianValue.find()[0]['value']))

averageValue = col.map_reduce(mapf, reduceAverage, 'out')
print('Average: ' + str(averageValue.find()[0]['value']))

# stantardValue = col.map_reduce(mapf, reduceStandard, 'out')
# print('Standard Deviation: ' + str(stantardValue.find()[0]['value']))