#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:03:57 2017

@author: dkopa
Purpose: Quick reference to read and write files in different formats
"""

import h5py
import numpy as np

######## Data (matrix) read and write into python numpy compressed format file
mypyFileName = 'test.npz'

# Read/Load
npzfile = np.load(mypyFileName)
X = npzfile['X']
y = npzfile['y']

# Write
np.savez(mypyFileName, X=X, y=y)

######## Data (matrix) read and write into h5 file

myH5FileName = 'test.h5'

# Read hdf5 file ...
h5f = h5py.File(myFileName, 'r')
X = np.asarray(h5f['X'][()])
y = np.asarray(h5f['y'][()])

# Writing/Creating HDF5 dataset ...
with h5py.File(myFileName, 'w') as f:
    f['X'] = X
    f['y'] = y
    

######## Information read and write into text file
myTxtFileName = 'test.txt'

# Read
f_handle = open(myTxtFileName,'r')
lines = f_handle.readlines()
f_handle.close()

# Write
f_handle = open(myTxtFileName,'a')
f_handle.writelines('writing line ...' + '\n')
f_handle.close()