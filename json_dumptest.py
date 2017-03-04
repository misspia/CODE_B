#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 05:46:47 2017

@author: enochou
"""
"""
input dictionary


data={"name":"poop"}

import json
with open('filename.json', 'w') as fp:
    json.dump(data, fp)


import datetime
datetime.datetime.now()
x = status.input()


"""
#Import


#json.load()
#with open('strings.json') as json_data:
#    d = json.load(json_data)
"""
with open("minedata.json") as f:
    content = f.readlines()
    content = [x.strip() for x in content] 
"""
import json

def which_quad(x,y):
    if x <= 5000 and y <= 5000:
        return 1
    if x > 5000 and y <= 5000:
        return 2
    if x > 5000 and y > 5000:
        return 3
    if x <= 5000 and y > 5000:
        return 4

def for_pia1():
    mylist=[]
    f=open("minedata.json")
    for line in f:
        mylist.append(json.loads(line))
        
    minecount = 0
    for i in range(len(mylist)):
        if i == 0:
            exportlist = [{"Time":i,"Q1":0,"Q2":0,"Q3":0,"Q4":0}]
        
        if len(mylist[i]) > minecount:
            quad1num = 0
            quad2num = 0
            quad3num = 0
            quad4num = 0
            for z in range(len(mylist[i])):
                quad=which_quad(mylist[i][z]["x"],mylist[i][z]["y"])
                if quad == 1:
                    quad1num += 1
                elif quad == 2:
                    quad2num += 1
                elif quad == 3:
                    quad3num += 1
                else:
                    quad4num += 1
            
            exportlist.append({"Time":i,"Q1":quad1num,"Q2":quad2num,"Q3":quad3num,"Q4":quad4num})
            minecount = len(mylist[i])
        else:
            exportlist.append({"Time":i,"Q1":exportlist[i-1]["Q1"],"Q2":exportlist[i-1]["Q2"],"Q3":exportlist[i-1]["Q3"],"Q4":exportlist[i-1]["Q4"]})
    
    return exportlist
    #with open('minedataforpia.json', 'w') as fp:
    #    json.dump(exportlist, fp)

"""
for i in range(len())


[{"Time":0,"Q1":0,"Q2":0,"Q3":0,"Q4":0},{"Time":1,"Q1":1,"Q2":2,"Q3":3,"Q4":4}

[]
height=10000
width=10000

#Export
"""