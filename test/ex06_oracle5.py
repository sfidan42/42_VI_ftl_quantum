import math
from math import pi
import qiskit as q
from qiskit import QuantumCircuit

nqubits = 5
oracle = QuantumCircuit(nqubits, name='oracle$_\omega$')

oracle.ch(0,2)
oracle.ccx(1,3,2)
oracle.ch(0,2)

oracle.to_gate()

# Add it to your circuit with (and remove your personal oracle):
search_algo_circuit.append(oracle, range(nqubits))

# Note
# Yes it is the same Oracle as the previous one, but since the circuit is 1 length bigger, there will be 2 solutions as result
# Solution is 1/√(2)(|01111⟩+|11111⟩)