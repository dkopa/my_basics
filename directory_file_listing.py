#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:01:36 2017

@author: dkopa
Purpose: Access files in subdirectories ...
"""

import os

mydir = '/home/hasnat/caffe/'

dirList = [x for x in os.listdir(mydir) if os.path.isdir(mydir+x)]

numOfDir = len(dirList)

for idc in range(numOfDir):
    print('========')
    tCurrDir = mydir+dirList[idc]+'/'
    print(dirList[idc])
    print('========')
    
    tFileList = [x for x in os.listdir(tCurrDir) if os.path.isfile(tCurrDir+x)]
    # tFileList = os.listdir(mydir+dirList[idc])
    numOfFiles = len(tFileList)
    
    for fc in range(numOfFiles):
        print(tCurrDir + tFileList[fc])
        # DO FURTHER PROCESSING ON EACH FILE