from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import Initialize
from imageloader_V1 import getImageandPad
import numpy as np
import matplotlib.pyplot as plt

normalized_Image = getImageandPad().flatten()

image_Vector = normalized_Image / np.linalg.norm(normalized_Image)

num_qubits = int(np.ceil(np.log2(len(image_Vector))))
num_elemnts_req = 2**num_qubits

# Vektor auf die nächste Potenz von 2 auffüllen
padded_vector = np.zeros(num_elemnts_req)
padded_vector[:len(image_Vector)] = image_Vector

print("We require this number of qubits: ", num_qubits)
qc = QuantumCircuit(num_qubits)

qc.initialize(padded_vector, range(num_qubits))
print(qc.decompose().draw('text'))