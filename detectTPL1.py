#!/usr/bin/env python
# coding=utf-8

import os 
import json

appPath = "/home/zhanxian/workspace/LibID/profiles/app/"

libPath = "/home/zhanxian/workspace/LibID/profiles/Lib9/"

outputPath = "./outputs/"

appList = os.listdir(appPath)

libList = os.listdir(libPath)

for app in appList:

    eachappPath = os.path.join(appPath,app)

    eachoutAppPath = os.path.join("outputs/Lib9/",app)
    if os.path.exists(eachoutAppPath):
        print "this app .." + app + "has handled!"
        continue
    print eachoutAppPath

    cmd = "./LibID.py detect -af {0} -ld {1} -o {2}".format(eachappPath,libPath,"outputs/Lib9/")
    os.system(cmd)



print "all work is done!" 



