from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from tensorflow import keras as ks
import numpy as np
from qiskit.circuit.library import Initialize

def main():
    print('Process Started') #Start Meldung

    #Load important stuff
    (x_train,y_train), (x_test,y_train) = ks.datasets.mnist.load_data()


main()

