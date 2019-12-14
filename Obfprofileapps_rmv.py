#!/usr/bin/env python
# coding=utf-8

import os
import time 

appPath = "/home/zhanxian/workspace/LibID/data/obfuscate_each/rmv/"

appList = os.listdir(appPath)

profilePath = "/home/zhanxian/workspace/LibID/obfuscation/tech/rmv/"

for app in appList:
    eachAppPath = os.path.join(appPath,app)

    startTime=time.time()

    appname = app.split(".apk")[0]

    eachProfilePath = os.path.join(profilePath,appname+".json")

    if os.path.exists(eachProfilePath):
        continue

    cmd = "python {0} profile -f {1} -o {2}".format("/home/zhanxian/workspace/LibID/LibID.py",eachAppPath,"./tech/rmv/")
    os.system(cmd)

    endtime=time.time()

    elapse=endtime-startTime

    cmd = "echo {0},{1}>>{2}".format(app,elapse,"Techrmv_oriappProfileTime.csv")
    os.system(cmd)

print "all work is done!"

