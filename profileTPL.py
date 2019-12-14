#!/usr/bin/env python
# coding=utf-8

import os
import time

TPLPath = "/home/zhanxian/workspace/TPLdetect/standard_repo/"

TPLProfilePath = "/home/zhanxian/workspace/LibID/profiles/lib"
TPLList = os.listdir(TPLPath)

for tpl in TPLList:

    eachTPLPath = os.path.join(TPLPath,tpl)
    
    if tpl.endswith(".jar"):
        tplname = tpl.split(".jar")[0]
    elif tpl.endswith('.aar'):
        tplname = tpl.split(".aar")[0]
    else:
        print "this is not an Android TPL"
        print tpl 
        cmd = "cmd {0}>>{1}".format(tpl,"wrongTPL")
        os.system(cmd)

    jsontplPath = os.path.join(TPLProfilePath,tplname+".json")

    if os.path.exists(jsontplPath):
        continue
    
    start = time.time()

    cmd = "./LibID.py profile -f {0}".format(eachTPLPath)
    os.system(cmd)

    end = time.time()

    elapse = end-start

    cmd = "echo {0},{1}>>{2}".format(tpl,elapse,"TPLProfileTime.csv")
    os.system(cmd)


print "all work is done!"

