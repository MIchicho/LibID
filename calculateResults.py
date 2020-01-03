#!/usr/bin/env python
# coding=utf-8
#  Author  : Chicho
#  date    : 2019-12-31
#  function: we first run this parogram then run 2.parseLibResult.py
#            3. Acc.py  

import os
import json

resultPath = "./results"

LibListPath = "./outputs/"

if not os.path.exists(resultPath):
    os.makedirs(resultPath) 


LibList = os.listdir(LibListPath)

appProfilePath = "./profiles/app/"


appList = os.listdir(appProfilePath)


for app in appList:
    
    total_time = 0
    appLibList= []
    app_dict = {}

    appresultPath = os.path.join(resultPath, app)

    if os.path.exists(appresultPath):
        continue

    for lib in LibList:

        appPath = os.path.join(LibListPath,lib,app)

        print appPath

        if not os.path.exists(appPath):
            continue 

        f=open(appPath)

        load_dict = json.load(f)
        runtime = load_dict['time']
        total_time = total_time + float(runtime) 
        libs = load_dict['libraries']
  #      libnameList = libs['name']

        if len(libs)>0:
            appLibList = appLibList + libs
    
        f.close()




    app_dict['libraries'] = appLibList
    app_dict['time'] = total_time



    with open(appresultPath,"wa+") as f:
        json.dump(app_dict,f)

        print "finished file load ... " + app 


print "all work is done!"
