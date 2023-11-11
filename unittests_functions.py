# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:51:29 2023

@author: Chelsea Apawti
"""

import numpy as np
import unittest
from qutip import *
import circuit
import constants
import tableau
import random


# Unittest for storeGenerators
class testStoreGen(unittest.TestCase):

    def setUp(self):
        self.size = 2
        self.cir = circuit.Circuit(self.size)
        self.value = False
        self.cir.setStoreGenerators(self.value)
        self.result = self.cir.getStoreGenerators()

        print("The value going into setStoreGenerators is:", self.value)
        print("The value returned by getStoreGenerators is:", self.result)
        
        
    def testStoreGenerators(self):
        self.assertEqual(self.result, self.value, "storeGenerators did not pass the unittest")
        
if __name__ == '__main__':
    unittest.main()


# # Unittest for clearTableau
# class testClearTab(unittest.TestCase):
    
#     def setUp(self):
#         self.size = 2
        
#         self.tab = np.hstack(((np.identity(2*self.size)), np.zeros((2*self.size,1))))
#         self.tab = np.vstack((self.tab, np.zeros((1, 2*self.size + 1))))
#         print("Verification tableau:")
#         print(self.tab)
        
#         self.testTab = tableau.Tableau(self.size)
#         for i in range(2*self.size+1):
#             for j in range(2*self.size+1):
#                 self.testTab.tableau[i][j]=random.randint(0,1)
#         print("Random tableau:")
#         print(self.testTab.tableau)
        
#         self.testTab.clearTableau()
#         print("Random tableau after clearing:")
#         print(self.testTab.tableau)
        
        
#     def testClearTableau(self):
#         for i in range(2*self.size+1):
#             for j in range(2*self.size+1):
#                 self.assertEqual(self.tab[i][j], self.testTab.tableau[i][j], "clearTableau did not pass the unittest")
                
# if __name__ == '__main__':
#     unittest.main()


# # Unittest for applyGates
# class testApplyGates(unittest.TestCase):
    
#     def setUp(self):
#         self.size = 2
#         self.cir = circuit.Circuit(self.size)
#         self.cir_tab = self.cir.getTableau
#         self.gen_test = tableau.Tableau.tableauToGenerators(self.cir_tab)  #<--- This doesn't want to work
        
#         self.cir.setStoreGenerators(True)
#         self.gates = np.array([constants.CGATE, 0, 1, constants.MGATE, 0, constants.HGATE, 1, constants.PGATE, 0])
#         self.cir.applyGates(self.gates)
#         self.gen_ver = self.cir.getGenerators
        
#         i = 0
#         gen_size = len(self.gen_test)
#         self.qc = QubitCircuit(N=size,num_cbits=1)
#         # For each set of (gate, qubit(s)), check type and run corresponding update method
#         while (i < self.gates.size):
#             if self.gates[i] == constants.HGATE:
#                 bit = self.gates[i+1]
#                 self.qc.add_gate("SNOT", targets = [bit])
#                 i += 2
#             elif self.gates[i] == constants.CGATE:
#                 controlbit = self.gates[i+1]
#                 targetbit = self.gates[i+2]
#                 self.qc.add_gate("CNOT", controls =controlbit, targets = targetbit)
#                 i += 3
#             elif self.gates[i] == constants.PGATE:
#                 bit = self.gates[i+1]
#                 self.qc.add_gate("S",targets = [bit])
#                 i += 2
#             elif self.gates[i] == constants.MGATE:
#                 bit = self.gates[i+1]
#                 self.qc.add_measurement("MO", targets = [bit],classical_store =0)
#                 i += 2
        
#         qubit = basis(2,0)
#         zerostate = qubit
#         for i in range(gen_size-1):
#             zerostate= tensor(zerostate,qubit)
#         result = self.qc.run(state=zerostate)
    
#         for i in range(gen_size):
#             gen = self.gen_test[i]
#             k=0
#             for j in gen:
#                 k=k+1
#                 if k==1:
#                     if   j =="+":
#                         sign = +1
#                     elif j =="-":
#                         sign = -1
#                 if k==2: #First character is always a '+ or a minus'
#                     if j == "I":
#                         mat = sign*qeye(2)
#                     elif j == "X":
#                         mat = sign*sigmax()
#                     elif j == "Y":
#                         mat = sign*sigmay()
#                     elif j == "Z":
#                         mat = sign*sigmaz()
#                 else:
#                     if j == "I":
#                         mat = tensor(mat,qeye(2))
#                     elif j == "X":
#                         mat = tensor(mat,sigmax())
#                     elif j == "Y":
#                         mat = tensor(mat,sigmay())
#                     elif j == "Z":
#                         mat = tensor(mat,sigmaz())
#             outputvec = mat*result
#             diffvec = outputvec-result
#             diff = np.linalg.norm(diffvec)
#             if diff == 0:
#                 print(gen + " is a stabilizer")
#             else:
#                 print("Something went wrong with " + gen)

    
#     def test_ApplyGates(self):
#           self.assertEqual(self.gen_test, self.gen_ver, "applyGates did not pass the unittest")

# if __name__ == '__main__':
#     unittest.main()
