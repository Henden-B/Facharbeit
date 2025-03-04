from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import Initialize
from imageloader_V1 import getImageandPad
import numpy as np
import matplotlib.pyplot as plt

qc = QuantumCircuit(10)
