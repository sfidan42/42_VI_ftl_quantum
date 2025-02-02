import numpy as np
import qiskit as q
from qiskit import QuantumCircuit

nqubits = 4
oracle = QuantumCircuit(nqubits, name='oracle$_\omega$')

# Balanced oracle
b = np.random.randint(1,2**nqubits-1)
b_str = format(b, '0'+str(nqubits-1)+'b')
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        oracle.x(qubit)

for qubit in range(nqubits-1):
    oracle.cx(qubit, nqubits-1)
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        oracle.x(qubit)

oracle.to_gate()
oracle.draw('mpl')

# Add it to your circuit with (and remove your personal oracle):
circuit.append(oracle, range(nqubits))

# Note
# The exercise asks to test with 4 qubits. But if the student has made a generic system, you can change nqubits.
# circuit is a QuantumCircuit