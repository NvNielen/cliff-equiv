# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:22:27 2023

@author: Chelsea Apawti
"""


import numpy as np

'test_tab has size (2q+1, 2q)'
test_tab = [[1,0,1,0,1],[0,1,0,1,0],[1,1,1,0,0],[0,0,1,1,1]]
n,m = np.shape(test_tab)
q = int((m-1)/2)


"Phase gate"
for x in range(n):
    test_tab[x][m-1] = test_tab[x][m-1] ^ (test_tab[x][0]*test_tab[x][q])
    test_tab[x][q] = test_tab[x][q] ^ test_tab[x][0]

print(test_tab)


# "Hadamard gate"
# for x in range(n):
#     test_tab[x][m-1] = test_tab[x][m-1] ^ (test_tab[x][0]*test_tab[x][q])
#     var = test_tab[x][q] 
#     test_tab[x][q] = test_tab[x][0]
#     test_tab[x][0] = var

# print(test_tab)