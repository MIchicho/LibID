#!/usr/bin/env python
# coding=utf-8

import os
import time 

appPath = "/home/zhanxian/workspace/TPLdetect/Apps/"

appList = os.listdir(appPath)

profilePath = "/home/zhanxian/workspace/LibID/profiles/app/"

for app in appList:
    eachAppPath = os.path.join(appPath,app)

    startTime=time.time()

    appname = app.split(".apk")[0]

    eachProfilePath = os.path.join(profilePath,appname+".json")

    if os.path.exists(eachProfilePath):
        continue

    cmd = "python {0} profile -f {1}".format("./LibID.py",eachAppPath)
    os.system(cmd)

    endtime=time.time()

    elapse=endtime-startTime

    cmd = "echo {0}>>{1}".format(elapse,"appProfileTime.csv")
    os.system(cmd)

print "all work is done!"

