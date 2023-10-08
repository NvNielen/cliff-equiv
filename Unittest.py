import numpy as np
import random
import unittest
import mgate
import phase
import Hgate
import CNOT
import tableau
import Verify_gen as vg
import tableau_to_gen as tg

class testMGate(unittest.TestCase):
    def test_rowsum(self):
        # Initialise tableau
        n = 2
        print("Initialising tableau with size n=" + str(n))
        tab = tableau.Tableau(n)
        tab.setTableau(np.array([
            [0,0,1,1,0],
            [1,1,1,1,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ]))

        # Apply method
        print("Applying rowsum(0,1) on tableau")
        print(tab.getTableau())
        mgate.rowsum(tab,0,1)

        # Verify
        self.assertTrue((tab.getTableau() == np.array([
            [1,1,0,0,1],
            [1,1,1,1,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ])).all() == True, "Rowsum on h=0, i=1 tested incorrectly")

        # Apply method
        print("Applying rowsum(2.3) on tableau")
        print(tab.getTableau())
        mgate.rowsum(tab,2,3)

        # Verify
        self.assertTrue((tab.getTableau() == np.array([
            [1,1,0,0,1],
            [1,1,1,1,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ])).all() == True, "Rowsum on h=0, i=1 tested incorrectly")


    def test_measurement(self):
        # Initialise tableau
        n = 2
        print("Initialising tableau with size n=" + str(n))
        tab = tableau.Tableau(n)
        tab.setTableau(np.array([
            [1,0,0,1,0],
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0]
        ]))

        # Apply method
        print("Applying measurement of qubit 0 on tableau")
        print(tab.getTableau())
        mgate.applyM(tab, 0)

        # Verify
        self.assertTrue((tab.getTableau() == np.array([
            [1,0,0,1,0],
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,1,1,1,0]
        ])).all() == True, "Measurement gate on qubit 0 tested incorrectly")

        # Apply method
        print("Applying measurement of qubit 1 on tableau")
        print(tab.getTableau())
        mgate.applyM(tab, 1)

        # Verify: measurement result is random so exclude last column
        self.assertTrue((tab.getTableau()[:,0:2*n] == np.array([
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
            # Initialise tableau with size n=q+1
            tab = tableau.Tableau(q+1)

            # Applying phase gate on qubit q
            phase.Phasegate(tab, q)
            gateInput = ["S", q]
            
            # Verify
            self.assertTrue(vg.verify_gen(tg.tableau_to_gen(tab), gateInput), "Phase gate for qubit " + str(q) + " tested incorrectly")
    def test_repeatingPhase(self):
        n = 100 # check 100 phase gates for size 100
        # Initialise tableau with size n and gateinput
        tab = tableau.Tableau(n)
        gateInput = []
        for q in range(n):
            # Applying phase gate on qubit q
            phase.Phasegate(tab, q)
            gateInput.append("S")
            gateInput.append(q)
            
        # Verify
        self.assertTrue(vg.verify_gen(tg.tableau_to_gen(tab), gateInput), "Phase gate for " + str(n) + " qubits tested incorrectly")

class TestApplyHadamard(unittest.TestCase):
    def test_hadamard(self):
        n = 100 # check hadamard gate for 100 different tableau sizes
        for q in range(n):
            # Initialise tableau with size n=q+1
            tab = tableau.Tableau(q+1)

            # Applying Hadamard gate on qubit q
            Hgate.applyHadamard(tab, q)
            gateInput = ["H", q]
            
            # Verify
            self.assertTrue(vg.verify_gen(tg.tableau_to_gen(tab), gateInput), "Hadamard gate for qubit " + str(q) + " tested incorrectly")
    def test_repeatingHadamard(self):
        n = 100 # check 100 hadamard gates for size 100
        # Initialise tableau with size n and gateinput
        tab = tableau.Tableau(n)
        gateInput = []
        for q in range(n):
            # Applying Hadamard gate on qubit q
            Hgate.applyHadamard(tab, q)
            gateInput.append("H")
            gateInput.append(q)
            
        # Verify
        self.assertTrue(vg.verify_gen(tg.tableau_to_gen(tab), gateInput), "Hadamard gate for " + str(n) + " qubits tested incorrectly")
			
class TestCNOT(unittest.TestCase):
    def test_cnot(self):
        n = 10 # check CNOT gate for 10 different tableau sizes
        for c in range(1,n):
            for t in range(c):
                # Initialise tableau with size n=c+1
                tab = tableau.Tableau(c+1)

                # Applying CNOT gate on control qubit c and target qubit t
                CNOT.updateCNOT(tab, c, t)
                gateInput = ["C", c, t]
                
                # Verify
                self.assertTrue(vg.verify_gen(tg.tableau_to_gen(tab), gateInput), "CNOT gate for control qubit " 
                + str(c) + " and target qubit " + str(t) + " tested incorrectly")
    def test_repeatingCNOT(self):
        n = 100 # check 100 CNOT gates for size 100
        # Initialise tableau with size n and gateinput
        tab = tableau.Tableau(n)
        gateInput = []
        for c in range(1,n):
            for t in range(c):
                # Applying CNOT gate on control qubit c and target qubit t
                CNOT.updateCNOT(tab, c, t)
                gateInput.append("C")
                gateInput.append(c)
                gateInput.append(t)
            
        # Verify
        self.assertTrue(vg.verify_gen(tg.tableau_to_gen(tab), gateInput), "CNOT gate for " 
                + str(n) + " qubits tested incorrectly")

class TestRandomGate(unittest.TestCase):
    def test_randomSequence(self):
        n = 100 # check for 100 different gates
        # Initialise tableau with size n
        tab = tableau.Tableau(n)
        gateInput = []
        for q in range(n):
            gate = random.randint(0,2)
            if gate == 0:
                # Applying CNOT gate on random control qubit c and target qubit t
                c = random.randint(0,n-1)
                t = c
                while t == c:
                    t = random.randint(0,n-1)
                CNOT.updateCNOT(tab, c, t)
                gateInput.append("C")
                gateInput.append(c)
                gateInput.append(t)
            elif gate == 1:
                # Applying Hadamard gate on random qubit q
                q = random.randint(0,n-1)
                Hgate.applyHadamard(tab, q)
                gateInput.append("H")
                gateInput.append(q)
            elif gate == 2:
                # Applying Phase gate on random qubit q
                q = random.randint(0,n-1)
                phase.Phasegate(tab, q)
                gateInput.append("S")
                gateInput.append(q)
            
        # Verify
        self.assertTrue(vg.verify_gen(tg.tableau_to_gen(tab), gateInput), "Random sequence of gates for n = " + str(n) + " qubits tested incorrectly")

if __name__ == '__main__':
    unittest.main()