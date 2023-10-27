# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:28:50 2023

@author: Wiggert
"""
import tableau
from qutip import *
import numpy as np

#Function to verify if a set of generators represents stabilisers
def verify_gen(generators):
    size = len(generators)
    gatelst=[]
    
    #Create a quantum circuit object
    qc = QubitCircuit(N=size,num_cbits=1)
    
    #Prompt the user to enter gate information
    input("You are now asked to enter which gates were in your circuit. Enter these gates in order from the first gate acting on the qubits to the last gate..")
    while True:
        gate = input("Enter gate: (H, S, CN or M) ")
        if gate == "H":    
            bit = int(input("Enter bit on which gate is performed: "))
            qc.add_gate("SNOT", targets = [bit])
        elif gate == "S":
            bit = int(input("Enter bit on which gate is performed: "))
            qc.add_gate("S",targets = [bit])
        elif gate == "M":
            bit = int(input("Enter bit on which gate is performed: "))
            qc.add_measurement("MO", targets = [bit],classical_store =0)
        elif gate == "CN":
            controlbit = int(input ("Enter control bit: "))
            targetbit = int(input ("Enter target bit: "))
            qc.add_gate("CNOT", controls =controlbit, targets = targetbit)
        else:
            print("Invalid gate")
            
        cont = input("Are there more gates? Type 'n' if not ")
        print("")
        
        
        if cont == 'n':
            break
    qubit = basis(2,0)
    zerostate=qubit
    
    #Create the initial state as a tensor product of qubits
    for i in range(size-1):
        zerostate= tensor(zerostate,qubit)
        
    #Run the quantum circuit to get the resulting state
    result = qc.run(state=zerostate)
    
    #Iterate through the generators
    for i in range(size):
        gen = generators[i]
        k=0
        for j in gen:
            k=k+1
            if k==1: #First character is always a '+ or a minus'
                if   j =="+":
                    sign = +1
                elif j =="-":
                    sign = -1
            if k==2: 
                if j == "I":
                    mat = sign*qeye(2)
                elif j == "X":
                    mat = sign*sigmax()
                elif j == "Y":
                    mat = sign*sigmay()
                elif j == "Z":
                    mat = sign*sigmaz()
            else:
                if j == "I":
                    mat = tensor(mat,qeye(2))
                elif j == "X":
                    mat = tensor(mat,sigmax())
                elif j == "Y":
                    mat = tensor(mat,sigmay())
                elif j == "Z":
                    mat = tensor(mat,sigmaz())
                    
        #Apply the generator to the result state
        outputvec = mat*result
        
        #Calculate the difference between the output state and the result state
        diffvec = outputvec-result
        diff = np.linalg.norm(diffvec)
        
        #Check if the difference is zero to determine if it's a stabilizer
        if diff == 0:
            print(gen + " is a stabilizer")
        else:
            print("Something went wrong with" + gen)

