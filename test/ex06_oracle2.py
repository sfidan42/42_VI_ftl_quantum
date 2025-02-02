import math
from math import pi
import qiskit as q
from qiskit import QuantumCircuit

nqubits = 3
oracle = QuantumCircuit(nqubits, name='oracle$_\omega$')

oracle.h(2)
oracle.ccx(0,1,2)
oracle.h(2)

oracle.to_gate()

# Add it to your circuit with (and remove your personal oracle):
search_algo_circuit.append(oracle, range(nqubits))

