#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:43:45 2017

@author: hasnat
rename files
"""

import os
my_path = '/home/my_path/'
tfiles = [x for x in os.listdir(my_path) if x.find('orig_name')>-1] 

for orig_name in tfiles:
    print(orig_name)
    rep_name = orig_name.replace('orig_name', 'rep_name')
    print(rep_name)
    os.rename(my_path+orig_name, my_path+rep_name)