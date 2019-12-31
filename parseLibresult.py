#!/usr/bin/env python
# coding=utf-8

import os
import json

appPath = "/home/zhanxian/workspace/LibDetection/LibID/results/"

appList = os.listdir(appPath)

for app in appList:

    eachappPath = os.path.join(appPath,app)

    f = open(eachappPath)

    load_dict = json.load(f)
    runtime = load_dict['time']

    libList = load_dict['libraries']

    cmd = "echo {0},{1}>>{2}".format(app,runtime,"runningTime.csv")
    os.system(cmd)

    LibNameList = []
    for lib in libList:
        libname = lib['name']
        LibNameList.append(libname)

    cmd = "echo {0},{1}>>{2}".format(app,",".join(LibNameList),"resultLibs.csv")
    os.system(cmd)


print "all work is done!"
