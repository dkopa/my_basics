#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:31:36 2017

@author: hasnat
"""
import numpy as np

acctaf = ['99.56 & 0.996', '99.62 & 0.997', '99.60 & 0.997', '99.55 & 0.996', '99.23 & 0.991']
j = 0

acc, taf = zip(*[(np.float32(acctaf[j].split(' & ')[0]), np.float32(acctaf[j].split(' & ')[1])) for j in range(len(acctaf))])
#acc = [np.float32(acctaf[j].split(' & ')[0]) for j in len(acctaf)]
#taf = [np.float32(acctaf[j].split(' & ')[1]) for j in len(acctaf)]


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
X = np.array(acc).reshape(-1, 1)
y = np.array(taf)            
lr.fit(X, y)