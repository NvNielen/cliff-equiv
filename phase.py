# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:22:27 2023

@author: Chelsea Apawti
"""


import numpy as np

# Tableau of the size 2*n+1 by 2*n
#test_tab = [[1,0,1,0,1],[0,1,0,1,0],[1,1,1,0,0],[0,0,1,1,1]]

# Rows and columns of the tableau
#r,c = np.shape(test_tab)
# Number of qubits
#n = int((c-1)/2)

def Phasegate(tab,qubit):
    "Phase gate"
    size = tab.getTableauSize() #Obtain size of tableau input
    tableau = tab.getTableau()  #Obtain array of tableau input
    r=2*size                    #This is how large the tableau is in the y-direction
    c= 2*size+1                 #This is how large the tableau is in the x direction
    n=size                      #This is how many qubits in the system described by the tableau
    test_tab=tableau
    for x in range(r): #Perform algorithm on each row in tableau
        test_tab[x,c-1] = np.logical_xor(test_tab[x,c-1],(test_tab[x,0]*test_tab[x,n])) #Updating 'r' in the rightmost column of the tableau
        test_tab[x,n] = np.logical_xor(test_tab[x,n],test_tab[x,0])                     #Updating the 'x' describing the generator of the qubit being affected
    return test_tab


#print(test_tab)


# "Hadamard gate"
# for x in range(n):
#     test_tab[x][m-1] = test_tab[x][m-1] ^ (test_tab[x][0]*test_tab[x][q])
#     var = test_tab[x][q] 
#     test_tab[x][q] = test_tab[x][0]
#     test_tab[x][0] = var

# print(test_tab)