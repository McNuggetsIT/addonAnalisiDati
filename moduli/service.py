import numpy as np

def readFileToArray(file_path):
    #restituisce subito l'array inserendo i valori tra i delimitatori
    #l'encoding serve se presenta formattazioni particolari
    return np.genfromtxt(file_path, delimiter= ",",  encoding="utf-8-sig", comments="#", dtype=float, invalid_raise=False)
    #array = []
    #expected_cols = None
    #with open(file_path, "r", encoding="utf-8-sig") as file:
    #    for line in file:
    #        parts = line.strip().split()
    #        if not parts: #Restituisce True se la lista è vuota e va al porrimo elemento
    #            continue
#
    #        #prima riga valida
    #        if expected_cols is None:
    #            expected_cols = len(parts)
#
    #        #inserisci solo se ha lo stesso numero di colonne
    #        if len(parts) == expected_cols:
    #            cleaned = []
    #            for p in parts:
    #                p = p.replace(",", ".")
    #                cleaned.append(float(p))
    #            array.append(cleaned) 
    #return array

def saveFileToCSV(file_path, array):
    scelta = int(input("Scegliere: \n1. Sovrascrivere il file\n2. Aggiungere al file\n"))
    mode = "w" if scelta == 1 else "a"

    if np.isscalar(array):
        array = np.array([array])

    with open(file_path, mode) as f:
        np.savetxt(f, array, delimiter=",", fmt="%.2f")

def verifyVector(A):
    dim = A.ndim
    if dim == 1:
        return True
    else:
        return False
