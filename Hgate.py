# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:50:58 2023

@author: rensk
"""
import numpy as np
import tableau

# size of n
#CONST_SIZE = 2

# Create standard tableau:
# a 2nx2n identity matrix stacked with a 2nx1 phase vector of zeros
#def createTableau():
 #   return np.hstack(((np.identity(2*CONST_SIZE)), np.zeros((2*CONST_SIZE,1))))


# Apply the Hadamard gate to a qubit in the tableau
def applyHadamard(tab, qubit_index):
    CONST_SIZE=tab.getTableauSize()
    tableau = tab.getTableau()
    
    for i in range(2 * CONST_SIZE):
        # Extract xia and zia
        xia = tableau[i, qubit_index]
        zia = tableau[i, qubit_index + CONST_SIZE]

        # Update 'ri' based on xia and zia
        tableau[i, 2 * CONST_SIZE] = np.logical_xor(tableau[i, 2 * CONST_SIZE], np.logical_and(xia, zia))



        # Swap xia and zia
        tableau[i, qubit_index] = zia
        tableau[i, qubit_index + CONST_SIZE] = xia

    return tableau

# Example usage:
#tableau = createTableau()
#print("Initial Tableau:")
#print(tableau)

# Apply Hadamard gate to qubit 'a' (replace 'a' with your desired qubit index)
#a = 0  # Change this value as needed
#tableau = applyHadamard(tableau, a)

#print("\nTableau after applying Hadamard gate to qubit", a)
#print(tableau)