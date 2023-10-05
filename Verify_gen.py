# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:28:50 2023

@author: Wiggert
"""
import tableau
from qutip import *
import numpy as np


#This function takes a list of generators, with each element of the list being a string representating a pauli operator
#The first character of a string is the sign, with subsequent characters representing pauli matrices
def verify_gen(generators):
    size = len(generators) #This is also the number of qubits in the system
    gatelst=[] 
    qc = QubitCircuit(N=size,num_cbits=1) #Initialising a quantum circuit. The user will add gates to this circuit.
    n=int(input("How many gates are in your circuit?")) 
    input("You are now asked to enter which gates were in your circuit. Enter these gates in ordef from the first gate acting on the qubits to the last gate. Press enter")
    k=0 #Counter to keep track of how many gates have been added
    while k<n: #Repeatedly ask the user for the input of a gate
        gate = input("Enter next gate: (H, S, CN or M) ") 
        if gate == "H":    
            bit = int(input("Enter bit on which gate is performed: "))
            qc.add_gate("SNOT", targets = [bit]) #This adds a specific gate to the circuit
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
            k=k-1 #We should'nt add a counter if a gate hasnt been added to the circuit.
            
        k=k+1
        print("")
    
    qubit = basis(2,0) #Initialising a qubit in the zero state
    zerostate=qubit
    for i in range(size-1): #Repeatedly tensoring the zero state with itself to make an n qubit system of all zero states.
        zerostate= tensor(zerostate,qubit)
    result = qc.run(state=zerostate) #Using the quantum circuit with the inputted gates to get a new state
    #print(result)
    
    
    #We now have the resulting vector state when a quantum circuit with the gates inputted is performed on the zero state
    #This resulting vector state should be the eigenvector of all of our generators
    #Now we need to turn our generators from the list into actual matrices
    for i in range(size): #Check one generator at a time
        gen = generators[i] 
        k=0
        for j in gen: 
            k=k+1
            if k==1: #The first character is the sign 
                if   j =="+":
                    sign = +1
                elif j =="-":
                    sign = -1
            if k==2: #Second character is the first matrix
                if j == "I":
                    mat = sign*qeye(2)
                elif j == "X":
                    mat = sign*sigmax()
                elif j == "Y":
                    mat = sign*sigmay()
                elif j == "Z":
                    mat = sign*sigmaz()
            else: #Subsequent matrices get tensored with previous matrices
                if j == "I":
                    mat = tensor(mat,qeye(2))
                elif j == "X":
                    mat = tensor(mat,sigmax())
                elif j == "Y":
                    mat = tensor(mat,sigmay())
                elif j == "Z":
                    mat = tensor(mat,sigmaz())
        outputvec = mat*result #We multiply the matrix by the previously found resulting vector
        diffvec = outputvec-result 
        diff = np.linalg.norm(diffvec) #Check if the two vectors are the same which would make it an eigenvector of the generator
        if diff == 0:
            print(gen + " is a stabilizer")
        else:
            print("Something went wrong with" + gen)
        #print(outputvec) 

#lst=["+ZI","+IZ"]
#verify_gen(lst)