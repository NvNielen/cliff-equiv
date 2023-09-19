import numpy as np

# size of n
CONST_SIZE = 2

# Create standard tableau:
# a 2nx2n identity matrix stacked with a 2nx1 phase vector of zeros
def createTableau():
    return np.hstack(((np.identity(2*CONST_SIZE)), np.zeros((2*CONST_SIZE,1))))

# Apply the CNOT update rules on given tableau using control and target qubits (which are indices here)
def updateCNOT(tableau, control, target):
    t = np.logical_xor(tableau[:, control + CONST_SIZE], np.ones((1,2*CONST_SIZE)))
    t = np.logical_xor(tableau[:, target], t)
    t = np.logical_and(tableau[:, control], np.logical_and(tableau[:, target + CONST_SIZE], t))
    tableau[:, 2*CONST_SIZE] = np.logical_xor(tableau[:, 2*CONST_SIZE], t)
    tableau[:, target] = np.logical_xor(tableau[:, target], tableau[:, control])
    tableau[:, control + CONST_SIZE] = np.logical_xor(tableau[:, control + CONST_SIZE], tableau[:, target + CONST_SIZE])
    return tableau

print(updateCNOT(createTableau(), 0, 1))