import numpy as np
import tableau

# Apply the CNOT update rules on given tableau using control and target qubits (which are indices here)
def updateCNOT(tab, control, target):
    size = tab.getTableauSize() #Obtain size from tableau
    tableau = tab.getTableau()  #Obtain array from tableau
    # For all i in {1,...,2n}, set r_i = r_i ⊕ x_i,control*z_i,target(x_i,target ⊕ z_i,control ⊕ 1)
    # Update rightmost column by performing algorithm one step at time
    t = np.logical_xor(tableau[:, control + size], np.ones((1,2*size + 1))) 
    t = np.logical_xor(tableau[:, target], t)
    t = np.logical_and(tableau[:, control], np.logical_and(tableau[:, target + size], t))
    tableau[:, 2*size] = np.logical_xor(tableau[:, 2*size], t)
    # Now rightmost column has been updated
    
    # For all i in {1,...,2n}, set x_i,target = x_i_target ⊕ x_i,control
    # Updating x and z column according to algorithm
    tableau[:, target] = np.logical_xor(tableau[:, target], tableau[:, control])
    
    # For all i in {1,...,2n}, set z_i,control = z_i,control ⊕ z_i,target
    tableau[:, control + size] = np.logical_xor(tableau[:, control + size], tableau[:, target + size])

#create tableau with n=2
#tab = tableau.Tableau(2)
# Apply CNOT update rules on tableau with control bit 0, target bit 1
#print(tab.getTableau())
#updateCNOT(tab, 0, 1)
#print(tab.getTableau())