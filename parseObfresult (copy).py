#!/usr/bin/env python
# coding=utf-8

import os 
import json

oriPath = "./obfu_tools/obf/"

fileList =  os.listdir(oriPath)

app_dict = {}

for app in fileList:
    appPath = os.path.join(oriPath,app)
    libList = []
    
    f = open(appPath)

    load_dict = json.load(f)

    run_time = load_dict['time']
    appName = load_dict['filename'].split("proguard-")[-1]
    libs = load_dict['libraries']

    cmd = "echo {0},{1}>>{2}".format(appName,str(run_time),"proguard_Time.csv")
    os.system(cmd)

    if len(libs)>0:
        for lib in libs:
            libName = lib['name']
            if libName not in libList:
                libList.append(libName)

        app_dict[appName] = libList

        cmd = "echo {0},{1}>>{2}".format(appName,",".join(libList),"proguard_TestResult.csv")
        os.system(cmd)
    else:
        app_dict[appName] = []
        cmd = "echo {0}:{1}>>{2}".format(appName,"","proguard_TestResult.csv")
#        os.system(cmd)



gtPath = "/home/zhanxian/workspace/LibDetection/LibID/outputs/obf/GroundTruth/obf_ground_truth.csv"

gtf=open(gtPath)
lines = gtf.readlines()
gtf.close()

gt_dict = {}

for line in lines:
    line = line.replace("\n","")

    segs = line.split(",")
    
    app = segs[0]
    
    del(segs[0])
     
    libs = segs 

    gt_dict[app]=libs 


for app in app_dict:

    if app in gt_dict.keys():
        
        
        test_libs = app_dict[app]
        gt_libs = gt_dict[app]
        

        intersec = list(set(test_libs).intersection(set(gt_libs)))
        rate = len(intersec)*1.0/len(gt_libs)

        
        cmd = "echo {0},{1},{2},{3}>>{4}".format(app,len(intersec),len(gt_libs),rate,"proguard_result.csv")
        os.system(cmd)



print ("all work is done!")
