#!/usr/bin/env python
# coding=utf-8
# author    : Chicho
# function  : Change the TPL name into group id: artifact id: version
#              and mv these TPL into the LibID challenge file 



import os

path = "../challenge/jars/"

outputPath = "./challenge/TPLs/"

for root,dirs,files in os.walk(path,topdown=False):

    if files != []:
        for file in files:
            TPLPath = os.path.join(root,file)
            if os.path.isfile(TPLPath):
                segs = TPLPath.split("/")
                newname = segs[-4] + "_" + segs[-3] + "_" + segs[-1]
                # group id, artifact id, version, library name
                cmd = "echo '{}','{}','{}','{}'>>{}".format(segs[-4],segs[-3],segs[-2],segs[-1],"challengeTPLinfo.csv")
                os.system(cmd)
  #              newnamePath = os.path.join(outputPath,newname)
                cmd = "cp {} {}".format(TPLPath,outputPath)
                os.system(cmd)

print "all work is done!"
