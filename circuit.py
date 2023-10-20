import numpy as np
import constants
import random
import tableau
import sys

class Circuit:
    # Create circuit with given qubits size, this size determines tableau size
    # Create tableau with given size, initiate gates array, storeGenerators
    # and generators array
    def __init__(self, size: int):
        while size <= 0:
            raise ValueError("You tried to create a circuit with a qubit-size of " + str(size) +
                              ". This is invalid. Try again by entering an integer larger than 0: ")
        self.qubitSize = size
        self.tableau = tableau.Tableau(size)
        # GATELIMIT determines maximum number of gates that can be applied
        self.gates = np.zeros((constants.GATELIMIT))
        # Keeps track of index of next available gate slot in gates array
        self.gateIndex = 0
        # Keeps track of number of gates
        self.numberOfGates = 0
        # Store measurement results in 1d array
        self.gateResults = np.zeros((constants.GATELIMIT), dtype=np.bool)
        # Store gate results index
        self.gateResultsIndex = 0
        # Store generators set to false by default
        self.storeGenerators = False
    """GETTERS"""
    # Get gates array
    def getGates(self):
        return self.gates
    # Get gate results array
    def getGateResults(self):
        return self.gateResults
    # Get total number of gates
    def getNumberOfGates(self):
        return self.numberOfGates
    # Get tableau
    def getTableau(self):
        return self.tableau
    # Get storeGenerators boolean value
    def getStoreGenerators(self):
        return self.storeGenerators
    # Get generators array
    def getGenerators(self):
        return self.generators
    """SETTERS"""
    # Set storeGenerators boolean value
    def setStoreGenerators(self, value: bool):
        if (value == True and not hasattr(self, 'generators')):
            self.clearGenerators()
        self.storeGenerators = value
    """METHODS"""
    # Apply the CNOT update rules on given tableau using control and target qubits (which are indices here)
    def applyCN(self, control, target):
        size = self.tableau.getTableauSize()
        tableau = self.tableau.getTableau()

        # For all i in {1,...,2n}, set r_i = r_i ⊕ x_i,control*z_i,target(x_i,target ⊕ z_i,control ⊕ 1)
        t = np.logical_xor(tableau[:2*size, control + size], np.ones((1,2*size), dtype=np.bool))
        t = np.logical_xor(tableau[:2*size, target], t)
        t = np.logical_and(tableau[:2*size, control], np.logical_and(tableau[:2*size, target + size], t))
        tableau[:2*size, 2*size] = np.logical_xor(tableau[:2*size, 2*size], t)

        # For all i in {1,...,2n}, set x_i,target = x_i_target ⊕ x_i,control
        tableau[:2*size, target] = np.logical_xor(tableau[:2*size, target], tableau[:2*size, control])
        
        # For all i in {1,...,2n}, set z_i,control = z_i,control ⊕ z_i,target
        tableau[:2*size, control + size] = np.logical_xor(tableau[:2*size, control + size], tableau[:2*size, target + size])
    # Apply the Hadamard gate to a qubit in the tableau
    def applyH(self, qubit):
        size = self.tableau.getTableauSize()
        tableau = self.tableau.getTableau()

        # Extract xia and zia
        xia = np.copy(tableau[:2*size, qubit])
        zia = np.copy(tableau[:2*size, qubit + size])

        # Update 'ri' based on xia and zia
        tableau[:2*size, 2*size] = np.logical_xor(tableau[:2*size, 2*size], np.logical_and(xia, zia))

        # Swap xia and zia
        tableau[:2*size, qubit] = zia
        tableau[:2*size, qubit + size] = xia
    # Apply CNOT gate update rules
    def applyP(self, qubit):
        size = self.tableau.getTableauSize()
        tableau = self.tableau.getTableau()

        # Extract xia and zia
        xia = tableau[:2*size, qubit]
        zia = tableau[:2*size, qubit + size]

        # Update 'ri' based on xia and zia
        tableau[:2*size,2*size] = np.logical_xor(tableau[:2*size,2*size], np.logical_and(xia,zia))
        
        # Update zia based on xia and zia
        tableau[:2*size, qubit + size] = np.logical_xor(zia,xia)
    # A helper function for applyM() that takes 4 bits as input, and that returns the exponent to which i is
    # raised (either 0, 1, or −1) when the Pauli matrices represented by x1z1 and x2z2 are multiplied
    # used for measurement gate update rules
    def rowsum(self, h, j):
        size = self.tableau.getTableauSize()
        tableau = self.tableau.getTableau()
        
        # For all k ∈ {1, . . . , n} set x_h,k = x_j,k ⊕ x_h,k
        tableau[h, :size] = np.logical_xor(tableau[j, :size], tableau[h, :size])
        
        # For all k ∈ {n, . . . , 2n} set z_h,k = z_j,k ⊕ z_h,k
        tableau[h, size:2*size] = np.logical_xor(tableau[j, size:2*size], tableau[h, size:2*size])
        
        # g(x_1, z_1, x_2, z_2) = 
        # 0, if x_1 = z_1 = 0 OR
        # z_2 - x_2, if x_1 = z_1 = 1 OR
        # z_2(2x_2 - 1), if x_1 = 1, z_1 = 0 OR
        # x_2(1 - 2z_2), if x_1 = 0, z_1 = 1
        g = np.where(tableau[j, :size] == tableau[j, size:2*size],
                    np.where(tableau[j, :size] == 0, np.zeros((1, size), dtype=np.bool), tableau[h, size:2*size] - tableau[h, :size]),
                    np.where(tableau[j, :size] == 0, tableau[h, :size]*(1 - 2*tableau[h, size:2*size]),
                            tableau[h, size:2*size]*(1 - 2*tableau[h, :size]))
                    )

        # r_h = ((2r_h + 2r_j + g) mod 4)/2
        tableau[h, 2*size] = ((2*tableau[h, 2*size] + 2*tableau[j, 2*size] + np.sum(g)) % 4)/2
    # Apply measurement gate update rules on qubit a for a given tableau
    def applyM(self, a):
        size = self.tableau.getTableauSize()
        tableau = self.tableau.getTableau()

        # retrieve entire column of qubit
        qubit = tableau[:2*size, a]

        # get i for {1,...,n} and p for {n+1,...,2n}
        i = np.argwhere(qubit[:size]).ravel()
        p = np.argwhere(qubit[size:2*size]).ravel() + size

        # check if a p was found
        if p.size != 0:
            # Case A: qubit a of the tableau in the range of x_(n+1)1 to x_(2n)1 has the value 1
            # In this case the measurement outcome is random, so the state needs to be updated.
            
            # First call rowsum(i,p) for all i in {1,...,2n} such that i=/=p and x_ia=1
            for item in np.append(i, p[1:]):
                self.rowsum(item, p[0])
            p = p[0]
            # Second, set entire the (p−n)th row equal to the pth row.
            # (Set every element in the row p-n equal to its equivalent element in row p)
            tableau[p - size][:] = tableau[p][:]

            # Third, set the pth row to be identically 0, except that r_p is 0 or 1 with equal probability, and z_pa=1.
            # (Set every element in row p equal to 0)
            tableau[p][:] = 0
            # (Set r_p (the last element in row p) equal to 0 or 1)
            tableau[p][2*size] = random.randint(0,1)
            # (Set z_pa equal to 1)
            tableau[p][a + size] = 1
            
            # Finally, return r_p as the measurement outcome. Increment gate results index
            self.gateResults[self.gateResultsIndex] = tableau[p][2*size]
            self.gateResultsIndex += 1
        else:
            # Case B: qubit a of the tableau in the range of x_(n+1)1 to x_(2n)1 contains no value 1
            # In this case the outcome is determinate, so measuring the state will not change it; the
            # only task is to determine whether 0 or 1 is observed. This is done as follows: 
                
            # First set the (2n+1)st row to be identically 0. 
            tableau[size*2][:] = 0
            
            # Second, call rowsum(2n+1,i+n) for all i in {1,...,n} such that x_ia=1.
            for index in range(size):
                self.rowsum(size*2, index + size)
                
            # Finally, return r_2n+1 as the measurement outcome. Increment gate results index
            self.gateResults[self.gateResultsIndex] = tableau[2*size][2*size]
            self.gateResultsIndex += 1
    # Gate abstract factory: given gate input, apply corresponding gate update rules
    # Gate input as follows: a linear list of gate type (0 to 3) followed by qubit and 
    # optionally extra qubit for CNOT
    # e.g. [0,1,2,2,1] -> CN on control qubit 1 and target qubit 0, then H on qubit 1
    def applyGates(self, gates):
        i = 0
        g = 1
        l = gates.size # size of gates array
        # The qubits for the gates are checked to have been selected correctly
        while (i < l):
            if gates[i] == constants.CGATE:
                if i+1 >= l or i+2 >= l:
                    raise IndexError("No target/control qubits given")
                elif gates[i+1]==gates[i+2]:
                    raise ValueError("The control and target qubit for gate " + str(g) + " have the same value")
                elif gates[i+1]>=self.qubitSize or gates[i+1]<0:
                    raise ValueError("The control qubit for gate " + str(g) + 
                                     " must be an integer in the range of 0 to " + str(self.qubitSize-1) + 
                                     " and cannot equal " + str(gates[i+2]) + " (target qubit)")
                elif gates[i+2]>=self.qubitSize or gates[i+2]<0:
                    raise ValueError("The target qubit for gate " + str(g) + " must be an integer in the range of 0 to " + 
                                     str(self.qubitSize-1) + " and cannot equal " + str(gates[i+1]) + "(control qubit)")
                else:
                    i += 3
                    g += 1
            elif gates[i] == constants.HGATE or gates[i] == constants.PGATE or gates[i] == constants.MGATE:
                if i+1 >= l:
                    raise IndexError("No qubit given")
                elif gates[i+1]>=self.qubitSize or gates[i+1]<0:
                    raise ValueError("The qubit for gate " + str(g) + " must be an integer in the range of 0 to " + str(self.qubitSize-1))
                else:
                    i += 2
                    g += 1
            else:
                raise ValueError("The value entered to specify gate " + g + " is invalid.")
        
        i = 0
        # For each set of (gate, qubit(s)), check type and run corresponding update method
        while (i < l):
            if gates[i] == constants.CGATE:
                self.applyCN(gates[i+1], gates[i+2])
                i += 3
            elif gates[i] == constants.HGATE:
                self.applyH(gates[i+1])
                i += 2
            elif gates[i] == constants.PGATE:
                self.applyP(gates[i+1])
                i += 2
            elif gates[i] == constants.MGATE:
                self.applyM(gates[i+1])
                i += 2
            self.numberOfGates += 1
            if self.storeGenerators: # if store generators, retrieve generator sets after each gate
                self.generators[self.numberOfGates,:,:] = self.tableau.tableauToGenerators()
        # Append gates to gates array
        self.gates[self.gateIndex:self.gateIndex+gates.size] = gates
        # Set gate index to new empty gate slot
        self.gateIndex += gates.size
    # Clear/set generators array
    def clearGenerators(self):
        size = self.tableau.getTableauSize()
        # Store max number of gates times nxn matrices of each state of the tableau in the circuit
        self.generators = np.zeros((round(constants.GATELIMIT/3),2*size,size+1))
        self.generators[self.numberOfGates,:,:] = self.tableau.tableauToGenerators()
    # Clear gates array, then clear corresponding tableau and possibly generators array
    def clearGates(self):
        # GATELIMIT determines maximum number of gates that can be applied
        self.gates = np.zeros((constants.GATELIMIT))
        # Reset gate index to zero
        self.gateIndex = 0
        # Reset measurement results
        self.gateResults = np.zeros((constants.GATELIMIT), dtype=np.bool)
        # Reset gate results index to zero
        self.gateResultsIndex = 0
        # Clear the tableau
        self.tableau.clearTableau()
        # Clear generator list if it exists
        if self.storeGenerators == True:
            self.clearGenerators()
    pass