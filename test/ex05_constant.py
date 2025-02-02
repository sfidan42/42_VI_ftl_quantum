import numpy as np
import qiskit as q
from qiskit import QuantumCircuit

nqubits = 4
oracle = QuantumCircuit(nqubits, name='oracle$_\omega$')

# Constant oracle
if np.random.randint(2) == 1:
    oracle.x(nqubits-1)

oracle.to_gate()
oracle.draw('mpl')

# Add it to your circuit with (and remove your personal oracle):
circuit.append(oracle, range(nqubits))

# Note
# The exercise asks to test with 4 qubits. But if the student has made a generic system, you can change nqubits.
# circuit is a QuantumCircuit