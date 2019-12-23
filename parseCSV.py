#!/usr/bin/env python
# coding=utf-8

import os

path = "/home/zhanxian/workspace/LibDetection/LibID/experiment/gt.csv"

f = open(path)

lines = f.readlines()

for line in lines:
    line = line.replace("\n","")

    libList = []

    segs = line.split(",")

    for seg in segs:

        if not seg=="":
            libList.append(seg)

    cmd = "echo {0}>>{1}".format(",".join(libList),"newgt.csv")
    os.system(cmd)

print "all work is done!"
