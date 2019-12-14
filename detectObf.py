#!/usr/bin/env python
# coding=utf-8


import os

cmd1 = "./LibID.py detect -ad ./obfuscation/tech/origin/ -ld ./obfuscation/libs/lib/ -o ./obfuscation/tech/outputs/origin/"

#os.system(cmd1)


cmd2 = "./LibID.py detect -ad ./obfuscation/tech/pkgFltn// -ld ./obfuscation/libs/lib/ -o ./obfuscation/tech/outputs/pkgFltn/"
#os.system(cmd2)

cmd3 = "./LibID.py detect -ad ./obfuscation/tech/ctrl/ -ld ./obfuscation/libs/lib/ -o ./obfuscation/tech/outputs/ctrl/"
#os.system(cmd3)

cmd4 = "./LibID.py detect -ad ./obfuscation/tech/rmv/ -ld ./obfuscation/libs/lib/ -o ./obfuscation/tech/outputs/rm/"
os.system(cmd4)
