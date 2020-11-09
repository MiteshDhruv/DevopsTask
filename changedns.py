#!/usr/bin/env python
# coding: utf-8
import os
import json
from collections import namedtuple
from json import JSONEncoder
cmd = "./coredns -conf Corefile" #to start the coredns service as the script runs 
def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

#Assume you received this JSON response
#studentJsonData = '{"name" : "sub2" , "type" : "A" , "ttl" : "1h" , "data" : ["127.0.0.11"] }'
changedns = input("Enter your command in the form of Json file or json format. It should be in format Name :  , Type :  , ttl :  , data : ")
# Parse JSON into an object with attributes corresponding to dict keys.
#student = json.loads(studentJsonData, object_hook=customStudentDecoder)

print("After Converting JSON Data into Custom Python Object")
change= print(changedns.name, changedns.type,changedns.ttl,changedns.data)

f = open("db.test.com", "w")
f.write(change)
f.close()

#open and read the file after the appending:
f = open("db.test.com", "r")
print(f.read())



