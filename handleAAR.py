#!/usr/bin/env python
# coding=utf-8
#  author     : Chicho 
#  Date       : 2020-10-30 
#  function   : change all aar format into jar format to let LibID can handle it 

import os
import zipfile

TPLPath = "./challenge/TPLs/"

aarPath = "/home/chicho/workspace/LibDetection/LibID/challenge/aarfiles"

if not os.path.exists(aarPath):
    os.makedirs(aarPath)


tplList = os.listdir(TPLPath)

for tpl in tplList:

    eachTPLPath = os.path.join(TPLPath,tpl)

    if tpl.endswith(".aar"):
  #      print tpl 

        TPLname = tpl.split(".aar")[0]
        newTPLPath = os.path.join(TPLPath,TPLname)
        os.rename(eachTPLPath,newTPLPath)
#        cmd = "unzip {0} -d {1}".format(eachTPLPath,newTPLPath)
        # no need zip format can handle it 
        z= zipfile.ZipFile(newTPLPath,'r')
        
        stpath = os.path.join(aarPath,TPLname+'.jar')

        for file in z.namelist():
            if file.endswith(".jar"):
                f=open(stpath,'w+')
                f.write(z.read(file))
                f.close()
            
        z.close()

        os.rename(newTPLPath,eachTPLPath)
    else:

        cmd = "cp {} {}".format(eachTPLPath, aarPath)
        os.system(cmd)


print "all work is done!"





