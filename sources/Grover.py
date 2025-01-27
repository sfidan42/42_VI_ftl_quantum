from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

# Multicontrolled Z gate
def mcz(circuit, qubits):
    if len(qubits) == 2:
        circuit.cz(qubits[0], qubits[1])
    else:
        circuit.h(qubits[-1])
        circuit.mcx(qubits[:-1], qubits[-1])
        circuit.h(qubits[-1])

# Grover's algorithm: Oracle
def oracle(circuit, marked_state):
    n = len(marked_state)
    qubits = range(n)
    for i in qubits:
        if marked_state[i] == '0':
            circuit.x(i)
    mcz(circuit, list(qubits))
    for i in qubits:
        if marked_state[i] == '0':
            circuit.x(i)
    circuit.barrier()

# Grover's algorithm: Diffuser
def diffuser(circuit, marked_state):
    n = len(marked_state)
    qubits = range(n)
    circuit.h(qubits)
    circuit.x(qubits)
    mcz(circuit, list(qubits))
    circuit.x(qubits)
    circuit.h(qubits)
    circuit.barrier()

def init_grover(marked_state):
    n = len(marked_state)
    qubits = range(n)
    qr = QuantumRegister(n)
    cr = ClassicalRegister(n)
    qc = QuantumCircuit(qr, cr)
    qc.h(qubits)
    qc.barrier()
    return qc
