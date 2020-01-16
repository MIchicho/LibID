#!/usr/bin/env python
# coding=utf-8


import os
import zipfile

TPLPath = "/media/chicho/Transcend/workspace/LibDetection/Performance/TPL-Files/standard_repo/"

aarPath = "/home/chicho/workspace/LibDetection/LibID/aarfiles"

if not os.path.exists(aarPath):
    os.makedirs(aarPath)


tplList = os.listdir(TPLPath)

for tpl in tplList:

    if tpl.endswith(".aar"):

        print tpl 

        eachTPLPath = os.path.join(TPLPath,tpl)
        
        TPLname = tpl.split(".aar")[0]
        newTPLPath = os.path.join(TPLPath,TPLname)
        os.rename(eachTPLPath,newTPLPath)
#        cmd = "unzip {0} -d {1}".format(eachTPLPath,newTPLPath)
         
        z= zipfile.ZipFile(newTPLPath,'r')
        
        stpath = os.path.join(aarPath,TPLname+'.jar')

        for file in z.namelist():
            if file.endswith(".jar"):
                f=open(stpath,'w+')
                f.write(z.read(file))
                f.close()
            
        z.close()

        os.rename(newTPLPath,eachTPLPath)

print "all work is done!"





