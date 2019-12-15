import pymongo
import json
from bson.code import Code
from bson.son import SON
import os
import csv

# Function to parse data
def uploadData(dataset, collection):
    print('Uploading Selected Data '+dataset+' to MongoDB')
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
        col.insert_one(row)
    print('Upload Completed Successfully')


# myclient = pymongo.MongoClient("mongodb://76.67.179.162:27017/")
myclient = pymongo.MongoClient("mongodb://192.168.2.14:27017/")
mydb = myclient["hadoop"]
col = mydb["MapReduceData"]

#choose Dataset to work with
while(True):
    print('Select Data Set: \n1 - NDBench-Training\n2 - NDBench-Testing \n3 - Test Data')
    datatype_in = input()
    if(datatype_in == '1' or datatype_in == '2' or datatype_in == '3'):
        break

# upload csv file to mongodb
while(True):
    print('Upload .CSV file to MongoDB (y\\n)')
    upload_in = input()
    if(upload_in =='y' or upload_in =='n'):
        if(upload_in == 'y'):
            if(datatype_in == '1'):
                uploadData('NDBench-training.csv', col)
            elif(datatype_in == '2'):
                uploadData('NDBench-testing.csv', col)
            elif(datatype_in == '3'):
                uploadData('test.csv', col)
        break

# select attribute
while(True):
    print('Select Attribute: \n1 - CPUUtilization_Average\n2 - NetworkIn_Average\n3 - NetworkOut_Average\n4 - MemoryUtilization_Average')
    attribute_in = input()
    if(attribute_in =='1' or attribute_in =='2' or attribute_in =='3' or attribute_in =='4'):
        break

if(attribute_in == '1'):
    mapf = Code(open('mapCPU.js', 'r').read())
elif(attribute_in == '2'):
    mapf = Code(open('mapNetworkIn.js', 'r').read())
elif(attribute_in == '3'):
    mapf = Code(open('mapNetworkOut.js', 'r').read())
elif(attribute_in == '4'):
    mapf = Code(open('mapMemory.js', 'r').read())



reduceMin = Code(open('reduceMin.js', 'r').read())
reduceMax = Code(open('reduceMax.js', 'r').read())
reduceMedian = Code(open('reduceMedian.js', 'r').read())
reduceAverage = Code(open('reduceAverage.js', 'r').read())
reduceStandard = Code(open('reduceStat.js', 'r').read())
finalizeStandard = Code(open('finalizeStandardDeviation.js', 'r').read())

out = mydb["out"]


minValue = col.map_reduce(mapf, reduceMin,'out')
print('Min: ' + str(minValue.find()[0]['value']))

maxValue = col.map_reduce(mapf, reduceMax, 'out')
print('Max: ' + str(maxValue.find()[0]['value']))

medianValue = col.map_reduce(mapf, reduceMedian, 'out')
print('Median: ' + str(medianValue.find()[0]['value']))

avgValue = col.map_reduce(mapf, reduceAverage, 'out')
print('Average: ' + str(avgValue.find()[0]['value']))

stantardValue = col.map_reduce(mapf, reduceStandard, finalize = finalizeStandard, out='out')
print('Standard Deviation: ' + str(stantardValue.find()[0]['value']))