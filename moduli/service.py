import numpy as np

def readFileToArray(file_path):
    #restituisce subito l'array inserendo i valori tra i delimitatori
    #l'encoding serve se presenta formattazioni particolari
    return np.genfromtxt(file_path, delimiter= ",",  encoding="utf-8-sig", comments="#", dtype=float)


def verifyVector(A):
    dim = A.ndim
    if dim == 1:
        return True
    else:
        return False
