import numpy as np
import random
import constants
import unittest
import circuit
import Verify_gen as vg

class testMGate(unittest.TestCase):
    def test_rowsum(self):
        # Initialise circuit with tableau size 2n + 1 x 2n + 1
        n = 2
        cir = circuit.Circuit(n)
        cir.getTableau().setTableau(np.array([
            [0,0,1,1,0],
            [1,1,1,1,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ]))

        # Apply method
        cir.rowsum(0,1)

        # Verify
        self.assertTrue((cir.getTableau().getTableau() == np.array([
            [1,1,0,0,1],
            [1,1,1,1,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ])).all() == True, "Rowsum on h=0, i=1 tested incorrectly")

        # Apply method
        cir.rowsum(2,3)

        # Verify
        self.assertTrue((cir.getTableau().getTableau() == np.array([
            [1,1,0,0,1],
            [1,1,1,1,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ])).all() == True, "Rowsum on h=2, i=3 tested incorrectly")


    def test_measurement(self):
        # Initialise circuit
        n = 2
        cir = circuit.Circuit(n)
        cir.getTableau().setTableau(np.array([
            [1,0,0,1,0],
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0]
        ]))

        # Apply method
        cir.applyM(0)

        # Verify
        self.assertTrue((cir.getTableau().getTableau() == np.array([
            [1,0,0,1,0],
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ])).all() == True, "Measurement gate on qubit 0 tested incorrectly")

        # Apply method
        cir.applyM(1)

        # Verify: measurement result is random so exclude last column
        self.assertTrue((cir.getTableau().getTableau()[:,0:2*n] == np.array([
            [1,0,0,1],
            [0,1,0,1],
            [0,0,1,0],
            [0,0,0,1],
            [0,1,1,1]
        ])).all() == True, "Measurement gate on qubit 1 tested incorrectly")

class TestPhasegate(unittest.TestCase):
    def test_phase(self):
        n = 100 # check phase gate for 100 different tableau sizes
        for q in range(n):
            # Initialise circuit with size n=q+1
            cir = circuit.Circuit(q+1)

            # Applying phase gate on qubit q
            cir.applyGates(np.array([constants.PGATE,q]))
            
            # Verify
            self.assertTrue(vg.verify_gen(cir), "Phase gate for qubit " + str(q) + " tested incorrectly")
    def test_repeatingPhase(self):
        n = 100 # check 100 phase gates for size 100
        # Initialise circuit with size n and gateinput
        cir = circuit.Circuit(n)
        for q in range(n):
            # Applying phase gate on qubit q
            cir.applyGates(np.array([constants.PGATE,q]))
            
        # Verify
        self.assertTrue(vg.verify_gen(cir), "Phase gate for " + str(n) + " qubits tested incorrectly")

class TestApplyHadamard(unittest.TestCase):
    def test_hadamard(self):
        n = 100 # check hadamard gate for 100 different tableau sizes
        for q in range(n):
            # Initialise circuit with size n=q+1
            cir = circuit.Circuit(q+1)

            # Applying Hadamard gate on qubit q
            cir.applyGates(np.array([constants.HGATE,q]))
            
            # Verify
            self.assertTrue(vg.verify_gen(cir), "Hadamard gate for qubit " + str(q) + " tested incorrectly")
    def test_repeatingHadamard(self):
        n = 10 # check 100 hadamard gates for size 100
        # Initialise circuit with size n and gateinput
        cir = circuit.Circuit(n)
        for q in range(n):
            # Applying Hadamard gate on qubit q
            cir.applyGates(np.array([constants.HGATE,q]))
            
        # Verify
        self.assertTrue(vg.verify_gen(cir), "Hadamard gate for " + str(n) + " qubits tested incorrectly")
			
# class TestCNOT(unittest.TestCase):
    def test_cnot(self):
        n = 20 # check CNOT gate for 20 different tableau sizes
        for c in range(1,n):
            for t in range(c):
                # Initialise circuit with size n=c+1
                cir = circuit.Circuit(c+1)

                # Applying CNOT gate on control qubit c and target qubit t
                cir.applyGates(np.array([constants.CGATE, c, t]))
                
                # Verify
                self.assertTrue(vg.verify_gen(cir), "CNOT gate for control qubit " 
                + str(c) + " and target qubit " + str(t) + " tested incorrectly")
    def test_repeatingCNOT(self):
        n = 20 # check 20 + 19 + 18 + ... + 1 CNOT gates for size 20
        # Initialise circuit with size n and gateinput
        cir = circuit.Circuit(n)
        for c in range(1,n):
            for t in range(c):
                # Applying CNOT gate on control qubit c and target qubit t
                cir.applyGates(np.array([constants.CGATE, c, t]))
        # Verify
        self.assertTrue(vg.verify_gen(cir), "CNOT gate for " 
                + str(n) + " qubits tested incorrectly")

class TestRandomGate(unittest.TestCase):
    def test_randomSequence(self):
        n = 200 # check for 200 different gates
        # Initialise circuit with size n
        cir = circuit.Circuit(n)
        gateInput = [constants.HGATE, n-1] # initialize with gate on largest possible qubit for Stim
        for q in range(n):
            gate = random.randint(0,2)
            if gate == 0:
                # Applying CNOT gate on random control qubit c and target qubit t
                c = random.randint(0,n-1)
                t = c
                while t == c:
                    t = random.randint(0,n-1)
                gateInput.append(constants.CGATE)
                gateInput.append(c)
                gateInput.append(t)
            elif gate == 1:
                # Applying Hadamard gate on random qubit q
                qu = random.randint(0,n-1)
                gateInput.append(constants.HGATE)
                gateInput.append(qu)
            elif gate == 2:
                # Applying Phase gate on random qubit q
                qu = random.randint(0,n-1)
                gateInput.append(constants.PGATE)
                gateInput.append(qu)
        gateInput = np.array(gateInput) # load all gates and qubits into numpy array
        # Apply all gates
        cir.applyGates(gateInput)
        # Verify
        self.assertTrue(vg.verify_gen(cir), "Random sequence of gates for n = " + str(n) + " qubits tested incorrectly")

if __name__ == '__main__':
    unittest.main()