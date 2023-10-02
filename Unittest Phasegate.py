# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:11:24 2023

@author: rensk
"""

from qutip import *
import numpy as np
import unittest



class TestPhasegate(unittest.TestCase):

    def phasegatetest(self):
        n = int(input("Enter how many qubits there are: "))
        bit = int(input("Enter on which qubit the calculations are performed "))
        tab = tableau.Tableau(n)
        Phasegate(tab,bit)
        generators = tableau_to_gen(tab)
        size = len(generators)
        qc = QubitCircuit(N=size,num_cbits=1)   
        qc.add_gate("S", targets = [bit])
        qubit = basis(2,0)
        zerostate=qubit
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
                                                
        # Assert that the difference is 0 (within a small tolerance)
        self.assertAlmostEqual(diff, 0, delta=1e-9)
        

if __name__ == '__main__':
    unittest.main()
      