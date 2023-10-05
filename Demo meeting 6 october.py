# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:09:38 2023

@author: rensk
"""

from qutip import *
import numpy as np
import unittest
from qutip.qip.operations import cnot
from qutip.qip.circuit import QubitCircuit
import random
import tableau
# Create a tableau with 2 qubits
tab = tableau.Tableau(2)

# Apply a Hadamard gate to qubit 0
tab = applyHadamard(tab, 0)
print("After applying the Hadamard gate to qubit 0:")
print(tab.getTableau())

# Apply a CNOT gate with control qubit 0 and target qubit 1
updateCNOT(tab, 1, 0)
print("After applying the CNOT gate (1, 0):")
print(tab.getTableau())

#- morgen stap voor stap uitwerking op papier van deze gates. (check)
#daarna unitsteps aanpassen.

class TestApplyHadamard(unittest.TestCase):

    def test_applyHadamardtest(self):
        for n in range(2, 4):
            for bit in range(n-1):
                    tab = Tableau(n)
                    applyHadamard(tab,bit)
                    generators = tableau_to_gen(tab)
                    size = len(generators)
                    qc = QubitCircuit(N=size,num_cbits=1)   
                    qc.add_gate("SNOT", targets = [bit])
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