import math
from math import pi
import qiskit as q
from qiskit import QuantumCircuit

nqubits = 3
oracle = QuantumCircuit(nqubits, name='oracle$_\omega$')

oracle.ch(0,2)
oracle.cz(1,2)
oracle.ch(0,2)


oracle.to_gate()

# Add it to your circuit with (and remove your personal oracle):
search_algo_circuit.append(oracle, range(nqubits))

