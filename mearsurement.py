# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:40:37 2023

@author: Chelsea Apawti
"""

import numpy as np
import random

# Row: [x_11, ..., x_1n, z_11, ... , z_1n, r1]  --> elements 0 to (n-1) are x's, n to (2n-1) are z's, 2n is r
# Tableau has an extra row [0,0,0,0,0] as "scratch space" --> Size is 2*n+1 by 2*n+1

test_tab = [[1,0,1,0,1], [0,1,0,1,0], [1,1,1,0,0], [0,0,1,1,1], [0,0,0,0,0]]  # Case A
#test_tab = [[1,0,1,0,1], [0,1,0,1,0], [0,1,1,0,0], [0,0,1,1,1],[0,0,0,0,0]]  # Case B


# Rows and columns of the tableau
r,c = np.shape(test_tab)
# Number of qubits
n = int((c-1)/2)
# Variable to keep track wether Case A has happened to know if Case B has to be executed
var=0

# p is an element in the tableau in the range of x_(n+1)1 to x_(2n)1 
for x in range(n,2*n+1):
    
    # Case A: an element of the tableau in the range of x_(n+1)1 to x_(2n)1 has the value 1
    if test_tab[x][0]==1:
        var=1
        print("Case A")
        # Case A
        # In this case the measurement outcome is 
        # random, so the state needs to be updated. This is done as follows:
        
        # First call rowsum(i,p) for all i in {1,...,2n} such that i=/=p and x_ia=1 (a is the first qubit/column so x_ia=x_i1, z_ia=z_i1).  
            #...
        
        # Second, set entire the (p−n)th row equal to the pth row.
        # (Set every element in the row p-n equal to its equivalent element in row p)
        for y in range(0,2*n+1):
            test_tab[x-n][y]=test_tab[x][y]
        
        # Third, set the pth row to be identically 0, except that r_p is 0 or 1 with equal probability, and z_pa=1.
        # (Set every element in row p equal to 0)
        for y in range(0,2*n+1):
            test_tab[x][y]=0
        # (Set r_p (the last element in row p) equal to 0 or 1)
        test_tab[x][2*n]=random.randint(0,1)
        # (Set z_pa equal to 1)
        test_tab[x][n]=1
        
        # Finally, return r_p as the measurement outcome.
        outcome = test_tab[x][2*n]
        print(outcome)
        print(test_tab)
        break


# Case B: there is NO element of the tableau in the range of x_(n+1)1 to x_(2n)1 with the value 1
if var==0:
    print("Case B")
    # Case B
    # In this case the outcome is determinate, so measuring the state will not change it; the
    # only task is to determine whether 0 or 1 is observed. This is done as follows: 
        
    # First set the (2n+1)st row to be identically 0. 
    for y in range(0,2*n+1):
        test_tab[2*n][y]=0
       
    # Second, call rowsum(2n+1,i+n) for all i in {1,...,n} such that x_ia=1. 
        # ...
        
    # Finally, return r_2n+1 as the measurement outcome
    outcome = test_tab[2*n][2*n]
    print(outcome)
    print(test_tab)