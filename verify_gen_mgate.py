# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:28:50 2023

@author: Wiggert

Edited by Chelsea Apawti for M gate unittest
"""
import tableau
from qutip import *
import numpy as np

 
def verify_gen_mgate(generators,bit):
    size = len(generators)
    gatelst=[]
    qc = QubitCircuit(N=size,num_cbits=1)
    qc.add_measurement("MO", targets = [bit],classical_store =0)
    
    qubit = basis(2,0)
    zerostate = qubit
    for i in range(size-1):
        zerostate= tensor(zerostate,qubit)
    result = qc.run(state=zerostate)
    
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
            print("Something went wrong with " + gen)
    return generators[bit]
