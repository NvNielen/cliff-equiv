import numpy as np
import constants

class Tableau:
    # Create standard tableau where size is the number of qubits
    # call clearTableau to set to identity tableau
    def __init__(self, size):
        self.size = size
        self.clearTableau()
    # Get tableau size (value)
    def getTableauSize(self):
        return self.size
    # Get tableau data structure (reference)
    def getTableau(self):
        return self.tableau
    # Convert tableau to a set of generators
    # return this set of generators
    def tableauToGenerators(self):
        n = self.size
        generators = np.zeros((size, size))

        # Calculate sign for each r (at index 2n) in stabilizer part of tableau (n to 2n)
        sign = np.power(-1, tableau[n:2*n,2*n])

        # Create a 2D array with generators for each qubit
        # Each row in this array denotes a list of generators
        # corresponding to the tableau row, for each i,j in {0, ..., n-1}:
        # generators[i, j] = 
        # sign_i * I, if x_i,j = z_i,j = 0 OR
        # sign_i * Y, if x_i,j = z_i,j = 1 OR
        # sign_i * X, if x_i,j = 1, z_i,j = 0 OR
        # sign_i * Z, if x_i,j = 0, z_i,j = 1
        for j in range(n):
            generators[:,j] = np.where(tableau[n:2*n, j] == tableau[n:2*n, n+j],
                        np.where(tableau[n:2*n, j] == 0, np.ones((size, 1))*sign*constants.GENI, np.ones((size, 1))*sign*constants.GENY),
                        np.where(tableau[n:2*n, j] == 0, np.ones((size, 1))*sign*constants.GENX, np.ones((size, 1))*sign*constants.GENZ))
        return generators
    # Convert set of generators to tableau
    # store tableau in this class
    def generatorsToTableau(self):
        pass
    # Clear tableau; reset to a 2nx2n identity matrix 
    # horizontally stacked with a 2nx1 phase vector of zeros
    # and 1x2n "scratch space" vertically stacked
    # Total: (2n + 1) * (2n + 1), where n is the tableau size
    def clearTableau(self):
        self.tableau = np.hstack(((np.identity(2*size)), np.zeros((2*size,1))))
        self.tableau = np.vstack((self.tableau, np.zeros((1, 2*size + 1))))
    pass