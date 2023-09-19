import numpy as np

class Tableau:
    # Create standard tableau:
    # a 2nx2n identity matrix stacked with a 2nx1 phase vector of zeros
    def __init__(self, size):
        self.size = size
        self.tableau = np.hstack(((np.identity(2*size)), np.zeros((2*size,1))))
    # Get tableau data structure (reference)
    def getTableau(self):
        return self.tableau
    # Get tableau size (value)
    def getTableauSize(self):
        return self.size
    pass