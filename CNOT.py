import numpy as np
import tableau

# Apply the CNOT update rules on given tableau using control and target qubits (which are indices here)
def updateCNOT(tab, control, target):
    size = tab.getTableauSize()
    tableau = tab.getTableau()
    t = np.logical_xor(tableau[:, control + size], np.ones((1,2*size + 1)))
    t = np.logical_xor(tableau[:, target], t)
    t = np.logical_and(tableau[:, control], np.logical_and(tableau[:, target + size], t))
    tableau[:, 2*size] = np.logical_xor(tableau[:, 2*size], t)
    tableau[:, target] = np.logical_xor(tableau[:, target], tableau[:, control])
    tableau[:, control + size] = np.logical_xor(tableau[:, control + size], tableau[:, target + size])
    return tableau

#create tableau with n=2
#tab = tableau.Tableau(2)
# Apply CNOT update rules on tableau with control bit 0, target bit 1
#print(tab.getTableau())
#updateCNOT(tab, 0, 1)
#print(tab.getTableau())