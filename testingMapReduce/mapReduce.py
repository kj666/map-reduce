import pymongo
import json
from bson.code import Code
from bson.son import SON
import os
import csv

# myclient = pymongo.MongoClient("mongodb://76.67.179.162:27017/")

myclient = pymongo.MongoClient("mongodb://192.168.2.14:27017/")

mydb = myclient["hadoop"]

col = mydb["testing"]

