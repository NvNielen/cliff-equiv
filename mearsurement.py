# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:40:37 2023

@author: Chelsea Apawti
"""

import numpy as np
import random

test_tab = [[1,0,1,0,1], [0,1,0,1,0], [1,1,1,0,0], [0,0,1,1,1], [0,0,0,0,0]]  # Case A
#test_tab = [[1,0,1,0,1], [0,1,0,1,0], [0,1,1,0,0], [0,0,1,1,1],[0,0,0,0,0]]  # Case B

r,c = np.shape(test_tab)
n = int((c-1)/2)

for x in range(n,2*n-1):
    if test_tab[x][0]==1:
        print("Case A")
        #Case A
        # In this case the measurement outcome is 
        # random, so the state needs to be updated. This is done as follows:
        
        # First call rowsum(i,p) for all i in {1,...,2n} such that i=/=p and x_ia=1.  
            #...
        # Second, set entire the (p−n)th row equal to the pth row.
        for y in range(0,2*n):
            test_tab[x-n][y]=test_tab[x][y]
        # Third, set the pth row to be identically 0, except that r_p is 0 or 1 with equal probability, and z_pa=1.
        for y in range(0,2*n):
            test_tab[x][y]=0
        test_tab[x][2*n-1]=random.randint(0,1)
        test_tab[x][n]=1
        # Finally, return r_p as the measurement outcome.
        outcome = test_tab[x][2*n-1]
        print(outcome)
        print(test_tab)
        break
    else:
        print("Case B")
        #Case B
        # In this case the outcome is determinate, so measuring the state will not change it; the
        # only task is to determine whether 0 or 1 is observed. This is done as follows: 
        
        # First set the (2n+1)st row to be identically 0. 
        for y in range(0,2*n):
            test_tab[2*n][y]=0
        # Second, call rowsum(2n+1,i+n) for all i in {1,...,n} such that x_ia=1. 
            # ...
        # Finally, return r_2n+1 as the measurement outcome
        outcome = test_tab[2*n][2*n-1]
        print(outcome)
        print(test_tab)