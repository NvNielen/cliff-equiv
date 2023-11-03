# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:46:40 2023

@author: rensk
"""


from qutip import *
import numpy as np
import unittest

#Define a test case for the Phasegate
class TestPhasegate(unittest.TestCase):

    #Test function for the Phasegate
    def phasegatetest(self):
        #Prompt the user for the number of qubits
        n = int(input("Enter how many qubits there are: "))
        
        #Prompt the user for the qubit on which the calculations are performed
        bit = int(input("Enter on which qubit the calculations are performed "))
        
        #Create a tableau for n qubits
        tab = tableau.Tableau(n)
        
        #Apply the Phasegate to the tableau on the specified qubit
        Phasegate(tab, bit)
        
        #Convert the tableau to generators
        generators = tableau_to_gen(tab)
        
        #Determine the size of the generators
        size = len(generators)
        
        #Create a quantum circuit object
        qc = QubitCircuit(N=size, num_cbits=1)
        
        #Add a single-qubit S gate to the quantum circuit on the specified qubit
        qc.add_gate("S", targets=[bit])
        
        #Create a basis state for a single qubit
        qubit = basis(2, 0)
        
        #Initialize the initial state as a tensor product of single-qubit states
        zerostate = qubit
        for i in range(size - 1):
            zerostate = tensor(zerostate, qubit)
        
        #Run the quantum circuit to obtain the resulting state
        result = qc.run(state=zerostate)
        
        #Iterate through the generators
        for i in range(size):
            gen = generators[i]
            k = 0
            for j in gen:
                k = k + 1
                if k == 1:
                    if j == "+":
                        sign = +1
                    elif j == "-":
                        sign = -1
                if k == 2:  #First character is always a '+' or a '-'
                    if j == "I":
                        mat = sign * qeye(2)
                    elif j == "X":
                        mat = sign * sigmax()
                    elif j == "Y":
                        mat = sign * sigmay()
                    elif j == "Z":
                        mat = sign * sigmaz()
                else:
                    if j == "I":
                        mat = tensor(mat, qeye(2))
                    elif j == "X":
                        mat = tensor(mat, sigmax())
                    elif j == "Y":
                        mat = tensor(mat, sigmay())
                    elif j == "Z":
                        mat = tensor(mat, sigmaz())
            outputvec = mat * result
            diffvec = outputvec - result
            diff = np.linalg.norm(diffvec)
        
        #Assert that the difference is 0 (within a small tolerance)
        self.assertAlmostEqual(diff, 0, delta=1e-9)

#Run the unit tests if this script is executed
if __name__ == '__main__':
    unittest.main()

#Define a test case for the Measurement operation
class TestMeasurement(unittest.TestCase):

    #Test function for the Measurement operation
    def Measurementtest(self):
        #Prompt the user for the number of qubits
        n = int(input("Enter how many qubits there are: "))
        
        #Prompt the user for the qubit on which the measurement is performed
        bit = int(input("Enter bit on which gate is performed: "))
        
        #Create a tableau for n qubits
        tab = tableau.Tableau(n)
        
        #Update the tableau with a measurement on the specified qubit
        updateMeasurement(tab, bit)
        
        #Convert the tableau to generators
        generators = tableau_to_gen(tab)
        
        #Determine the size of the generators
        size = len(generators)
        
        #Create a quantum circuit object
        qc = QubitCircuit(N=size, num_cbits=1)
        
        #Add a measurement gate to the quantum circuit on the specified qubit
        qc.add_gate("MO", targets=[bit])
        
        #Create a basis state for a single qubit
        qubit = basis(2, 0)
        
        #Initialize the initial state as a tensor product of single-qubit states
        zerostate = qubit
        for i in range(size - 1):
            zerostate = tensor(zerostate, qubit)
        
        #Run the quantum circuit to obtain the resulting state
        result = qc.run(state=zerostate)
        
        #Iterate through the generators
        for i in range(size):
            gen = generators[i]
            k = 0
            for j in gen:
                k = k + 1
                if k == 1:
                    if j == "+":
                        sign = +1
                    elif j == "-":
                        sign = -1
                if k == 2:  # First character is always a '+' or a '-'
                    if j == "I":
                        mat = sign * qeye(2)
                    elif j == "X":
                        mat = sign * sigmax()
                    elif j == "Y":
                        mat = sign * sigmay()
                    elif j == "Z":
                        mat = sign * sigmaz()
                else:
                    if j == "I":
                        mat = tensor(mat, qeye(2))
                    elif j == "X":
                        mat = tensor(mat, sigmax())
                    elif j == "Y":
                        mat = tensor(mat, sigmay())
                    elif j == "Z":
                        mat = tensor(mat, sigmaz())
            
            #Apply the generator to the result state
            outputvec = mat * result
            diffvec = outputvec - result
            diff = np.linalg.norm(diffvec)
                                                
        #Assert that the difference is 0 (within a small tolerance)
        self.assertAlmostEqual(diff, 0, delta=1e-9)

#Run the unit tests if this script is executed
if __name__ == '__main__':
    unittest.main()

#Define a test case for the Hadamard gate operation
class TestApplyHadamard(unittest.TestCase):

    #Test function for the Hadamard gate operation
    def test_applyHadamardtest(self):
        #Prompt the user for the number of qubits
        n = int(input("Enter how many qubits there are: "))
        
        #Prompt the user for the qubit on which the Hadamard gate is applied
        bit = int(input("Enter on which qubit the calculations are performed "))
        
        #Create a tableau for n qubits
        tab = tableau.Tableau(n)
        
        #Apply the Hadamard gate to the tableau on the specified qubit
        applyHadamard(tab, bit)
        
        #Convert the tableau to generators
        generators = tableau_to_gen(tab)
        
        #Determine the size of the generators
        size = len(generators)
        
        #Create a quantum circuit object
        qc = QubitCircuit(N=size, num_cbits=1)
        
        #Add a single-qubit SNOT gate (Hadamard) to the quantum circuit on the specified qubit
        qc.add_gate("SNOT", targets=[bit])
        
        #Create a basis state for a single qubit
        qubit = basis(2, 0)
        
        #Initialize the initial state as a tensor product of single-qubit states
        zerostate = qubit
        for i in range(size - 1):
            zerostate = tensor(zerostate, qubit)
        
        #Run the quantum circuit to obtain the resulting state
        result = qc.run(state=zerostate)
        
        #Iterate through the generators
        for i in range(size):
            gen = generators[i]
            k = 0
            for j in gen:
                k = k + 1
                if k == 1:
                    if j == "+":
                        sign = +1
                    elif j == "-":
                        sign = -1
                if k == 2:  # First character is always a '+' or a '-'
                    if j == "I":
                        mat = sign * qeye(2)
                    elif j == "X":
                        mat = sign * sigmax()
                    elif j == "Y":
                        mat = sign * sigmay()
                    elif j == "Z":
                        mat = sign * sigmaz()
                else:
                    if j == "I":
                        mat = tensor(mat, qeye(2))
                    elif j == "X":
                        mat = tensor(mat, sigmax())
                    elif j == "Y":
                        mat = tensor(mat, sigmay())
                    elif j == "Z":
                        mat = tensor(mat, sigmaz())
            
            # Apply the generator to the result state
            outputvec = mat * result
            diffvec = outputvec - result
            diff = np.linalg.norm(diffvec)
                                                
        #Assert that the difference is 0 (within a small tolerance)
        self.assertAlmostEqual(diff, 0, delta=1e-9)

#Run the unit tests if this script is executed
if __name__ == '__main__':
    unittest.main()

#Define a test case for the CNOT gate operation
class TestCNOT(unittest.TestCase):

    #Test function for the CNOT gate operation
    def CNOTTest(self):
        #Prompt the user for the number of qubits
        n = int(input("Enter how many qubits there are: "))
        
        #Prompt the user for the control and target bits of the CNOT gate
        controlbit = int(input("Enter control bit: "))
        targetbit = int(input("Enter target bit: "))
        
        #Create a tableau for n qubits
        tab = tableau.Tableau(n)
        
        #Update the tableau with a CNOT gate using the specified control and target bits
        updateCNOT(tab, controlbit, targetbit)
        
        #Convert the tableau to generators
        generators = tableau_to_gen(tab)
        
        #Determine the size of the generators
        size = len(generators)
        
        #Create a quantum circuit object
        qc = QubitCircuit(N=size, num_cbits=1)
        
        #Add a CNOT gate to the quantum circuit with the specified control and target bits
        qc.add_gate("CNOT", controls=controlbit, targets=targetbit)
        
        #Create a basis state for a single qubit
        qubit = basis(2, 0)
        
        #Initialize the initial state as a tensor product of single-qubit states
        zerostate = qubit
        for i in range(size - 1):
            zerostate = tensor(zerostate, qubit)
        
        #Run the quantum circuit to obtain the resulting state
        result = qc.run(state=zerostate)
        
        #Iterate through the generators
        for i in range(size):
            gen = generators[i]
            k = 0
            for j in gen:
                k = k + 1
                if k == 1: #First character is always a '+' or a '-'
                    if j == "+":
                        sign = +1
                    elif j == "-":
                        sign = -1
                if k == 2:  
                    if j == "I":
                        mat = sign * qeye(2)
                    elif j == "X":
                        mat = sign * sigmax()
                    elif j == "Y":
                        mat = sign * sigmay()
                    elif j == "Z":
                        mat = sign * sigmaz()
                else:
                    if j == "I":
                        mat = tensor(mat, qeye(2))
                    elif j == "X":
                        mat = tensor(mat, sigmax())
                    elif j == "Y":
                        mat = tensor(mat, sigmay())
                    elif j == "Z":
                        mat = tensor(mat, sigmaz())
            
            #Apply the generator to the result state
            outputvec = mat * result
            diffvec = outputvec - result
            diff = np.linalg.norm(diffvec)
                                                
        #Assert that the difference is 0 (within a small tolerance)
        self.assertAlmostEqual(diff, 0, delta=1e-9)

#Run the unit tests if this script is executed
if __name__ == '__main__':
    unittest.main()