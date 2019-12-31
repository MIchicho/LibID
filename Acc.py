#!/usr/bin/env python
# coding=utf-8

import os
gtPath = "/home/zhanxian/workspace/LibDetection/LibID/experiment/newgt.csv"

TestPath = "/home/zhanxian/workspace/LibDetection/LibID/resultLibs.csv"

resultLib_dict = {}

gtLibdict = {}

f=open(gtPath)

gtlines = f.readlines()

f.close()

f=open(TestPath)
tlines = f.readlines()
f.close()

for line in gtlines:
    LibList = []
    line = line.replace("\n","")
    segs = line.split(",")
    app = segs[0]
    del(segs[0])

    if (len(segs) == 1) and (segs[0] == ''):
        LibList = []
    else:
        LibList = segs

    gtLibdict[app]=LibList


for line in tlines:
    LibList = []
    line = line.replace("\n","")
    segs = line.split(",")
    app = segs[0].split(".json")[0]

    del(segs[0])

    if (len(segs) == 1) and (segs[0] == ''):
        LibList = []
    else:
        LibList = segs

    resultLib_dict[app]=LibList


for app in gtLibdict:

    if app in resultLib_dict.keys():
        gtLibList = gtLibdict[app]

        testLibList = resultLib_dict[app]

        TP = len(list(set(gtLibList).intersection(set(testLibList))))
        FP = len(testLibList) - TP 
        FN = len(gtLibList) - TP 

        cmd = "echo {0},{1},{2},{3}>>{4}".format(app,TP,FP,FN,"Acc_result.csv")
        os.system(cmd)


print "all work is done!"

