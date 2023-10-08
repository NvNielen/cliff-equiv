import tableau
import stim
import numpy as np

# This function takes a list of generators, with each element of the list being a string representating a pauli operator
# The first character of a string is the sign, with subsequent characters representing pauli matrices
# Next, it parses an input array of gates and corresponding qubits. This circuit is then simulated in Stim and the generators from the
# resulting tableau are extracted and compared to the generator list
def verify_gen(generators, inputarray):
    size = len(generators) # This is also the number of qubits in the system
    circuit = stim.Circuit() # Initialising a quantum circuit. The inputarray will add gates to this circuit.
    k=0
    while k < len(inputarray): # Repeatedly check the input of a gate
        gate = inputarray[k]
        if gate == "H":    
            bit = int(inputarray[k+1])
            circuit.append("H", [bit]) # This adds a specific gate to the circuit
            k += 2
        elif gate == "S":
            bit = int(inputarray[k+1])
            circuit.append("S", [bit])
            k += 2
        elif gate == "C":
            controlbit = int(inputarray[k+1])
            targetbit = int(inputarray[k+2])
            circuit.append("CNOT", [controlbit, targetbit])
            k += 3
        else:
            raise
    # Using the quantum circuit with the inputted gates to get a new state or tableau,
    # From this we get the strings of generators
    x2x, x2z, z2x, z2z, x_signs, z_signs = stim.Tableau.from_circuit(circuit).to_numpy()

    stabilizers = np.where(np.logical_not(np.logical_or(z2x, z2z)), "I", 
                np.where(np.logical_and(z2x, z2z), "Y",
                np.where(z2x == True, "X", "Z")))

    stabilizers = np.char.add(np.where(z_signs == True, "-", "+"), np.array([''.join(row) for row in stabilizers]))

    destabilizers = np.where(np.logical_not(np.logical_or(x2x, x2z)), "I", 
                np.where(np.logical_and(x2x, x2z), "Y",
                np.where(x2x == True, "X", "Z")))

    destabilizers = np.char.add(np.where(x_signs == True, "-", "+"), np.array([''.join(row) for row in destabilizers]))
    # Now we check the total list of destabilizer and stabilizer generators compared to the generator list
    if size > 1:
        return (np.concatenate((destabilizers,stabilizers)) == generators).all()
    else:
        return np.concatenate((destabilizers,stabilizers)) == generators