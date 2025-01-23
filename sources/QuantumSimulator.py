from qiskit_aer import Aer
from qiskit import transpile

def qsim(circuit):
    backend = Aer.get_backend('qasm_simulator')  # Get the Aer simulator
    circuit = transpile(circuit, backend)  # Optimize and transpile
    result = backend.run(circuit, shots = 500).result()  # 500 shots
    counts = result.get_counts(circuit)
    return counts
