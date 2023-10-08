# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:50:58 2023

@author: rensk
"""
import numpy as np
import tableau

# Apply the Hadamard gate to a qubit in the tableau
def applyHadamard(tab, qubit):
    size = tab.getTableauSize()
    tableau = tab.getTableau()

    # Extract xia and zia
    xia = np.copy(tableau[:2*size, qubit])
    zia = np.copy(tableau[:2*size, qubit + size])

    # Update 'ri' based on xia and zia
    tableau[:2*size, 2*size] = np.logical_xor(tableau[:2*size, 2*size], np.logical_and(xia, zia))

    # Swap xia and zia
    tableau[:2*size, qubit] = zia
    tableau[:2*size, qubit + size] = xia

# Example usage:
#tableau = createTableau()
#print("Initial Tableau:")
#print(tableau)

# Apply Hadamard gate to qubit 'a' (replace 'a' with your desired qubit index)
#a = 0  # Change this value as needed
#tableau = applyHadamard(tableau, a)