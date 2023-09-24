# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:28:50 2023

@author: Wiggert
"""
import tableau
from qutip import *
import numpy as np

def verify_gen(generators):
    size = len(generators)
    gatelst=[]
    qc = QubitCircuit(N=size,num_cbits=1)
    input("You are now asked to enter which gates were in your circuit. Enter these gates in ordef from the first gate acting on the qubits to the last gate..")
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
    for i in range(size-1):
        zerostate= tensor(zerostate,qubit)
    result = qc.run(state=zerostate)
    #print(result)
    
    for i in range(size):
        gen = generators[i]
        k=0
        for j in gen:
            k=k+1
            if k==1:
                if   j =="+":
                    sign = +1
                elif j =="-":
                    sign = -1
            if k==2: #First character is always a '+ or a minus'
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
        outputvec = mat*result
        diffvec = outputvec-result
        diff = np.linalg.norm(diffvec)
        if diff == 0:
            print(gen + " is a stabilizer")
        else:
            print("Something went wrong with" + gen)
        #print(outputvec) 
