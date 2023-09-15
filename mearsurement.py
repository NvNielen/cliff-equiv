# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:40:37 2023

@author: Chelsea Apawti
"""

import numpy as np

test_tab = [[1,0,1,0,1], [0,1,0,1,0], [1,1,1,0,0], [0,0,1,1,1]]

n,m = np.shape(test_tab)
q = int((m-1)/2)

for x in range(q,2*q-1):
    if test_tab[x][0]==1:
        #Case A
        print(x)
        print("Case A")
        break
    else:
        #Case B
        print("Case B")