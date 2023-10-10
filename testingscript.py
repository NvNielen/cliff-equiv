import numpy as np
import circuit
import constants

# new test code here

# Create circuit with 2 qubits
cir = circuit.Circuit(2)
#print(cir.getTableau().getTableau())
cir.setStoreGenerators(True)
# Apply CNOT on control 0 and target 1, M on 0, H on 1 and P on 0 consectutively
#cir.applyGates(np.array([constants.CGATE, 0, 1, constants.MGATE, 0, constants.HGATE, 1, constants.PGATE, 0]))
cir.applyGates(np.array([constants.HGATE,0]))
#print(cir.getTableau().getTableau())
print(cir.getGenerators())
# Get number of gates in circuit, should be 4
#print(cir.getNumberOfGates())