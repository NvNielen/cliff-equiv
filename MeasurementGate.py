import numpy as np
import tableau

def rowsum(tab, h, j):
    size = tab.getTableauSize()
    tableau = tab.getTableau()
    tableau[h, :size] = np.logical_xor(tableau[j, :size], tableau[h, :size])
    tableau[h, size:2*size] = np.logical_xor(tableau[j, size:2*size], tableau[h, size:2*size])
    g = np.where(tableau[j, :size] == tableau[j, size:2*size],
                 np.where(tableau[j, :size] == 0, np.zeros((1, size)), tableau[h, size:2*size] - tableau[h, :size]),
                 np.where(tableau[j, :size] == 0, tableau[h, :size]*(1 - 2*tableau[h, size:2*size]),
                          tableau[h, size:2*size]*(1 - 2*tableau[h, :size]))
                )
    tableau[h, 2*size] = ((2*tableau[h, 2*size] + 2*tableau[j, 2*size] + np.sum(g)) % 4)/2