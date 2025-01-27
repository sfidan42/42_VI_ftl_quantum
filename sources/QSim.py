from qiskit_ibm_runtime import QiskitRuntimeService, Session
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

def QBackend(qc, shots=500):

    # Initialize account.
    service = QiskitRuntimeService()

    # Backend and pass manager.
    backend = service.least_busy(operational=True, simulator=False)
    pm = generate_preset_pass_manager(target=backend.target, optimization_level=1)

    # Transpile the circuits using the pass manager.
    isa_circuit = pm.run(qc)

    # Submit the circuits to the IBM Runtime service.
    with Session(backend=backend) as session:
        # Submit a request to the Sampler primitive within the session.
        sampler = Sampler(mode=session)
        job = sampler.run([isa_circuit], shots=shots)
        pub_result = job.result()[0]
        counts = pub_result.data.c.get_counts()
        print(f"Counts: {counts}")
        return counts

from qiskit import transpile
from qiskit_aer import Aer

def QSimulator(qc, shots=500):
    backend = Aer.get_backend('qasm_simulator')
    qc = transpile(qc, backend)
    result = backend.run(qc, shots=shots).result()
    counts = result.get_counts(qc)
    return counts
