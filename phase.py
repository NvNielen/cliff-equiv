import numpy as np

def Phasegate(tab,qubit):
    size = tab.getTableauSize()
    tableau = tab.getTableau()

    # Extract xia and zia
    xia = tableau[:2*size, qubit]
    zia = tableau[:2*size, qubit + size]

    # Update 'ri' based on xia and zia
    tableau[:2*size,2*size] = np.logical_xor(tableau[:2*size,2*size],(xia*zia))
    
    # Update zia based on xia and zia
    tableau[:2*size, qubit + size] = np.logical_xor(zia,xia)