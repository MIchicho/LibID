#!/usr/bin/env python
# coding=utf-8

import json
import os

resultPath = "./result"

outputsPath = "./outputs/"

if not os.path.exists(resultPath):
    os.makedirs(result)

LibList = os.listdir(outputsPath)



LibPath = os.path.join(outputsPath,Lib)

appList = os.listdir(LibPath)

for app in appList:

    total_time = 0
    appLibList = []
    app_dict = []
    appPath = os.path.join(LibPath,app)
    
    f=open(appPath)

    load_dict = json.load(f)
    runtime = load_dict['time']
    total_time = total_time + runtime 
    libs = load_dict['libraries']
    appLibList = appLibList + libs 
    
    f.close()
    for i in range(1,len(LibList)):

        Lib_i = LibList[i]

        newappList = os.listdir(Lib_i)

        if app in newappList:

            newappPath = os.path.join(outputsPath,LibList[i],app)
            f= open(newappPath)

            load_dict = json.load(f)
            f.close()

            runtime = load_dict['time']
            total_time = runtime
            libs = load_dict['libraries']
            appLibList = appLibList + libs 
            

    app_dict['libraries'] = appLibList
    app_dict['time'] = total_time

    appresultPath = os.path.join(resultPath,app)

    with open(appresultPath,"wa+") as f:
        json.dump(app_dict,f)
        print "finished file load ... " + app 


print "all work is done!"

