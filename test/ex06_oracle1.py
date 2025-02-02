import math
from math import pi
import qiskit as q
from qiskit import QuantumCircuit

nqubits = 2
oracle = QuantumCircuit(nqubits, name='oracle$_\omega$')

theta = pi # theta can be anything (pi is chosen arbitrarily)
oracle.ry(theta/2,1)
oracle.cx(0,1)
oracle.ry(-theta/2,1)
oracle.cx(0,1)

oracle.to_gate()

# Add it to your circuit with (and remove your personal oracle):
search_algo_circuit.append(oracle, range(nqubits))