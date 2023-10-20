import circuit
import constants
import stim
import numpy as np

# This function takes a list of generators, with each element of the list being a string representating a pauli operator
# The first character of a string is the sign, with subsequent characters representing pauli matrices
# Next, it parses an input array of gates and corresponding qubits. This circuit is then simulated in Stim and the generators from the
# resulting tableau are extracted and compared to the generator list
def verify_gen(circuit):
    generators = circuit.getTableau().tableauToGenerators()
    gates = circuit.getGates() # get gates array from circuit
    stimCircuit = stim.Circuit() # Initialising a quantum circuit. The inputarray will add gates to this circuit.
    k=0
    gateCounter = 0
    while gateCounter < circuit.getNumberOfGates(): # Repeatedly check the input of a gate
        gate = gates[k]
        if gate == constants.HGATE:
            bit = int(gates[k+1])
            stimCircuit.append("H", [bit]) # This adds a specific gate to the circuit
            k += 2
            gateCounter += 1
        elif gate == constants.PGATE:
            bit = int(gates[k+1])
            stimCircuit.append("S", [bit])
            k += 2
            gateCounter += 1
        elif gate == constants.CGATE:
            controlbit = int(gates[k+1])
            targetbit = int(gates[k+2])
            stimCircuit.append("CNOT", [controlbit, targetbit])
            k += 3
            gateCounter += 1
        else:
            raise
    # Using the quantum circuit with the inputted gates to get a new state or tableau,
    # From this we get the strings of generators
    x2x, x2z, z2x, z2z, x_signs, z_signs = stim.Tableau.from_circuit(stimCircuit).to_numpy()

    stabilizers = np.where(np.logical_not(np.logical_or(z2x, z2z)), constants.GENI, 
                np.where(np.logical_and(z2x, z2z), constants.GENY,
                np.where(z2x == True, constants.GENX, constants.GENZ)))
    
    stabilizers = np.hstack((stabilizers, np.where(z_signs == True, -1, 1).reshape(z_signs.size, 1)))

    destabilizers = np.where(np.logical_not(np.logical_or(x2x, x2z)), constants.GENI, 
                np.where(np.logical_and(x2x, x2z), constants.GENY,
                np.where(x2x == True, constants.GENX, constants.GENZ)))

    destabilizers = np.hstack((destabilizers, np.where(x_signs == True, -1, 1).reshape(x_signs.size, 1)))
    # Now we check the total list of destabilizer and stabilizer generators compared to the generator list
    allstabilizers = np.vstack((destabilizers,stabilizers))
    return (allstabilizers == generators).all()