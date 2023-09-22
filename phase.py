# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:22:27 2023

@author: Chelsea Apawti
"""


import numpy as np

# Tableau of the size 2*n+1 by 2*n
test_tab = [[1,0,1,0,1],[0,1,0,1,0],[1,1,1,0,0],[0,0,1,1,1]]

# Rows and columns of the tableau
r,c = np.shape(test_tab)
# Number of qubits
n = int((c-1)/2)


"Phase gate"
for x in range(r):
    test_tab[x][c-1] = test_tab[x][c-1] ^ (test_tab[x][0]*test_tab[x][n])
    test_tab[x][n] = test_tab[x][n] ^ test_tab[x][0]

print(test_tab)


# "Hadamard gate"
# for x in range(n):
#     test_tab[x][m-1] = test_tab[x][m-1] ^ (test_tab[x][0]*test_tab[x][q])
#     var = test_tab[x][q] 
#     test_tab[x][q] = test_tab[x][0]
#     test_tab[x][0] = var

# print(test_tab)