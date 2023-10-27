# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:25:12 2023

@author: Wiggert
"""
#Import necessary functions and modules
from Hgate import applyHadamard as H
from CNOT import updateCNOT as CN
from phase import Phasegate as S
from Verify_gen import verify_gen as vg
from Tableau_to_gen import tableau_to_gen as tg
import tableau

#Set the number of qubits (in this case, 2)
n = 2

#Create a tableau for n qubits
tab = tableau.Tableau(n)

#Apply a CNOT gate to the tableau with control qubit 1 and target qubit 0
CN(tab, 1, 0)

#Uncomment the following lines to apply additional gates (Hadamard and Phase)
#H(tab, 0)
#S(tab, 0)

# Print the tableau's state representation
print(tab.getTableau())

# Convert the tableau to a list of generators
print(tg(tab))

# Verify if the generators represent stabilizers
vg(tg(tab))

