#!/usr/bin/env python
# coding=utf-8

import os 
import json
from random import shuffle 

appPath = "/home/zhanxian/workspace/LibDetection/LibID/profiles/app/"

libPath = "/home/zhanxian/workspace/LibDetection/LibID/profiles/Lib1/"

outputPath = "./outputs/"

appList = os.listdir(appPath)

libList = os.listdir(libPath)


for app in appList:

    eachappPath = os.path.join(appPath,app)

    eachappOutPath = os.path.join("outputs/Lib1",app)

    print eachappOutPath

    if os.path.exists(eachappOutPath):
        print "this " + app + " has existed"
        continue 

    cmd = "./LibID.py detect -af {0} -ld {1} -o {2}".format(eachappPath,libPath,"outputs/Lib1/")
    os.system(cmd)



        

