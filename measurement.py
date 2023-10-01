import numpy as np
import random
import tableau

# A function that takes 4 bits as input, and that returns the exponent to which i is
# raised (either 0, 1, or −1) when the Pauli matrices represented by x1z1 and x2z2 are multiplied
# used for measurement gate update rules
def rowsum(tab, h, j):
    size = tab.getTableauSize()
    tableau = tab.getTableau()
    
    # For all k ∈ {1, . . . , n} set x_h,k = x_j,k ⊕ x_h,k
    tableau[h, :size] = np.logical_xor(tableau[j, :size], tableau[h, :size])
    
    # For all k ∈ {1, . . . , n} set z_h,k = z_j,k ⊕ z_h,k
    tableau[h, size:2*size] = np.logical_xor(tableau[j, size:2*size], tableau[h, size:2*size])
    
    # g(x_1, z_1, x_2, z_2) = 
    # 0, if x_1 = z_1 = 0 OR
    # z_2 - x_2, if x_1 = z_1 = 1 OR
    # z_2(2x_2 - 1), if x_1 = 1, z_1 = 0 OR
    # x_2(1 - 2z_2), if x_1 = 0, z_1 = 1
    g = np.where(tableau[j, :size] == tableau[j, size:2*size],
                 np.where(tableau[j, :size] == 0, np.zeros((1, size)), tableau[h, size:2*size] - tableau[h, :size]),
                 np.where(tableau[j, :size] == 0, tableau[h, :size]*(1 - 2*tableau[h, size:2*size]),
                          tableau[h, size:2*size]*(1 - 2*tableau[h, :size]))
                )

    # r_h = ((2r_h + 2r_j + g) mod 4)/2
    tableau[h, 2*size] = ((2*tableau[h, 2*size] + 2*tableau[j, 2*size] + np.sum(g)) % 4)/2

# Apply measurement gate update rules on qubit a for a given tableau
def updateMeasurement(tab, a):
    size = tab.getTableauSize()
    tableau = tab.getTableau()
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
        # Merge p (minus its first occurrence of 1, which is chosen to be p) and i into i and call rowsum
        if p.size > 1:
            rowsum(tab, np.append(i, p[1:]), p[0])
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
        
        # Finally, return r_p as the measurement outcome.
        return tableau[p][2*size]
    else:
        # Case B: qubit a of the tableau in the range of x_(n+1)1 to x_(2n)1 contains no value 1
        # In this case the outcome is determinate, so measuring the state will not change it; the
        # only task is to determine whether 0 or 1 is observed. This is done as follows: 
            
        # First set the (2n+1)st row to be identically 0. 
        tableau[size*2][:] = 0
        
        # Second, call rowsum(2n+1,i+n) for all i in {1,...,n} such that x_ia=1. 
        rowsum(tab, size*2, i + size)
            
        # Finally, return r_2n+1 as the measurement outcome
        return tableau[2*size][2*size]

# create tableau with n=2
tab = tableau.Tableau(2)

# Apply measurement update rules on tableau with qubit 0
updateMeasurement(tab, 1)
print(tab.getTableau())