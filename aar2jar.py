#!/usr/bin/env python
# coding=utf-8
####################################################################################
#  author   : Chicho
#  Date     : 2020-11-03
#  Function : Since LibID just can handle the jar file and cannot handle the aar file, therefore, 
#             we need to transform the aar into the format that LibID can handle the aar format
#             In fact, the aar format just has extra files such as the resources, AndroidManifest.xml and etc
#             compared with the jar format. Thus, we just need to extract the jar file from the aar file 
############################################################################

import os
import sys
import getopt
import zipfile 

TPLPath = "./challenge/TPLs/"
aarPath = "./challenge/aarfiles/"

def aar2jar(TPLPath,aarPath):

    if not os.path.exists(aarPath):
        os.makedirs(aarPath)

    tplList = os.listdir(TPLPath)

    for tpl in tplList:

        eachTPLPath = os.path.join(TPLPath,tpl)

        if tpl.endswith(".aar"):
            TPLname = tpl.split(".aar")[0]
            newTPLPath = os.path.join(TPLPath,TPLname)
            os.rename(eachTPLPath,newTPLPath)
            z = zipfile.ZipFile(newTPLPath,'r')

            jarPath = os.path.join(aarPath,TPLname + '.jar')

            for file in z.namelist():
                if file.endswith(".jar"):
                    f =open(jarPath,'w+')
                    f.write(z.read(file))
                    f.close()

            z.close()

            os.rename(newTPLPath,eachTPLPath)

        else:

            cmd = "cp {} {}".format(eachTPLPath,aarPath)
            os.system(cmd)


def main(argv):
    tips = '''
    Usage:

    chmod a+x aar2jar.py
    ./aar2jar.py -i <original_TPL_Path> -o <TPLPath_LibID_can_handle>

    or 
    python aar2jar.py -i <original_TPL_Path> -o <TPLPath_LibID_can_handle>
    '''
    try:
        opts,args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print tips
        sys.exit(2)


    for opt,arg in opts:
        if opt == '-h':
            print tips
            sys.exit()
        elif opt in ("-i", "--ifile"):
            TPLPath = arg
        elif opt in ("-o","--ofile"):
            aarPath = arg 

    return TPLPath,aarPath
        


if __name__ == "__main__":
    if len(sys.argv) == 1:
        aar2jar(TPLPath,aarPath)
    else:
        TPLPath,aarPath = main(sys.argv[1:])
        aar2jar(TPLPath,aarPath)
        
