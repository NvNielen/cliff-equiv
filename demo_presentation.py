# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:16:44 2023

@author: Chelsea
"""

import numpy as np
import circuit
import constants
from gen_to_text import genToText

# Ask for the number of qubits
q = int(input("Enter the qubit size of the system: "))
# Create circuit with q qubits
cir = circuit.Circuit(q)
print("A circuit with", q, "qubits has now been created")
print("The tableau looks as follows: ")
print(cir.getTableau().getTableau())
cir.setStoreGenerators(True)

i=0
gateArray = np.empty(constants.GATELIMIT)
print(" ")
print("You are now asked to enter which gates were in your circuit. Enter these gates in order from the first gate acting on the qubits to the last gate..")
while True:
    gate = input("Enter gate 'H', 'S', 'CN' or 'M'. Enter 'x' if you are done adding gates to the circuit: ")
    if gate == "H":    
        gateArray[i]=constants.HGATE
        i+=1
        bit = int(input("Enter bit on which the Hadamard gate is performed: "))
        gateArray[i]=bit
        i+=1
    elif gate == "S":
        gateArray[i]=constants.PGATE
        i+=1
        bit = int(input("Enter bit on which the phase gate is performed: "))
        gateArray[i]=bit
        i+=1
    elif gate == "M":
        gateArray[i]=constants.MGATE
        i+=1
        bit = int(input("Enter bit on which the measurement gate is performed: "))
        gateArray[i]=bit
        i+=1
    elif gate == "CN":
        gateArray[i]=constants.CGATE
        i+=1
        controlbit = int(input ("Enter control bit for the CNOT gate: "))
        gateArray[i]=controlbit
        i+=1
        targetbit = int(input ("Enter target bit for the CNOT gate: "))
        gateArray[i]=targetbit
        i+=1
    elif gate == 'x':
        break
    else:
        print("Invalid gate")
        

gates=np.array([None]*i)
for x in range(i):
    gates[x]=int(gateArray[x])


# Apply gates to circuit
cir.applyGates(gates)
# Print the new tableau
print(" ")
print("After applying the gates, the tableau looks as follows: ")
print(cir.getTableau().getTableau())
# Print the generators
print(" ")
print(genToText(cir.getGenerators()))


