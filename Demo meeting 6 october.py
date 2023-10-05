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
from Hgate import applyHadamard 
from CNOT import updateCNOT
from phase import Phasegate 
from verify_gen import verify_gen 
from Tableau_to_gen import tableau_to_gen 

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

#Eerst zelf testen en kijken hoe het werkt
class TestApplyHadamard(unittest.TestCase):

    def test_applyHadamardtest(self):
        n = int(input("Enter how many qubits there are: "))
        bit = int(input("Enter on which qubit the calculations are performed "))
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
    
class Testmeasurement(unittest.TestCase):

    def Measurementtest(self):
        n = int(input("Enter how many qubits there are: "))
        bit = int(input("Enter bit on which gate is performed: "))
        tab = tableau.Tableau(n)
        updateMeasurement(tab, bit)
        generators = tableau_to_gen(tab)
        size = len(generators)
        qc = QubitCircuit(N=size,num_cbits=1)   
        qc.add_gate("MO", targets = [bit])
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
    
class TestCNOT(unittest.TestCase):

    def CNOTTest(self):
        n = int(input("Enter how many qubits there are: "))
        controlbit = int(input ("Enter control bit: "))
        targetbit = int(input ("Enter target bit: "))
        tab = tableau.Tableau(n)
        updateCNOT(tab, control, target)
        generators = tableau_to_gen(tab)
        size = len(generators)
        qc = QubitCircuit(N=size,num_cbits=1)   
        qc.add_gate("CNOT", controls =controlbit, targets = targetbit)
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

class TestApplyHadamard(unittest.TestCase):

    def test_applyHadamardtest(self):
        for n in range(2, 5):
            for bit in range(n):
                with self.subTest(n=n, bit=bit):
                    tab = tableau.Tableau(n)
                    applyHadamard(tab, bit)
                    generators = tableau_to_gen(tab)
                    size = len(generators)
                    qc = QubitCircuit(N=size, num_cbits=1)   
                    qc.add_gate("SNOT", targets=[bit])
                    qubit = basis(2, 0)
                    zerostate = qubit
                    for i in range(size-1):
                        zerostate = tensor(zerostate, qubit)
                    result = qc.run(state=zerostate)
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
                        outputvec = mat * result
                        diffvec = outputvec - result
                        diff = np.linalg.norm(diffvec)
                        
                        # Assert that the difference is 0 (within a small tolerance)
                        self.assertAlmostEqual(diff, 0, delta=1e-9)

if __name__ == '__main__':
    unittest.main()
    
class Testmeasurement(unittest.TestCase):

    def Measurementtest(self):
        for n in range(2, 5):
            for bit in range(n):
                with self.subTest(n=n, bit=bit):
                    tab = tableau.Tableau(n)
                    updateMeasurement(tab, bit)
                    generators = tableau_to_gen(tab)
                    size = len(generators)
                    qc = QubitCircuit(N=size,num_cbits=1)   
                    qc.add_gate("MO", targets = [bit])
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
    
class TestCNOT(unittest.TestCase):

    def CNOTTest(self):
        for n in range(2, 5):
            for controlbit in range(n):
                for targetbit in range(n):
                    with self.subTest(n=n, controlbit=controlbit,targetbit=targetbit):
                        n = int(input("Enter how many qubits there are: "))
                        controlbit = int(input ("Enter control bit: "))
                        targetbit = int(input ("Enter target bit: "))
                        tab = tableau.Tableau(n)
                        updateCNOT(tab, control, target)
                        generators = tableau_to_gen(tab)
                        size = len(generators)
                        qc = QubitCircuit(N=size,num_cbits=1)   
                        qc.add_gate("CNOT", controls =controlbit, targets = targetbit)
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
    
class TestPhasegate(unittest.TestCase):

    def phasegatetest(self):
        for n in range(2, 5):
            for bit in range(n):
                with self.subTest(n=n, bit=bit):
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