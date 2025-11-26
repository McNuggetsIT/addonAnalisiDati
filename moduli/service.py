import numpy as np

def readFileToArray(file_path):
    #restituisce subito l'array inserendo i valori tra i delimitatori
    #l'encoding serve se presenta formattazioni particolari
    #return np.genfromtxt(file_path, delimiter= ",",  encoding="utf-8-sig", comments="#", dtype=float, invalid_raise=False)
    array = []
    expected_cols = None
    with open(file_path, "r", encoding="utf-8-sig") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue

            #prima riga valida
            if expected_cols is None:
                expected_cols = len(parts)

            #inserisci solo se ha lo stesso numero di colonne
            if len(parts) == expected_cols:
                cleaned = []
                for p in parts:
                    p = p.replace(",", ".")
                    cleaned.append(float(p))
                array.append(cleaned)
                
    return array

def saveFileToCSV(file_path, array):
    type_write = int(input("Scegliere: \n1. Sovrascrivere il file\n2. Aggiungere al file\n"))
    if type_write == 1:
        type_write = "w"
    else:
        type_write = "a"
    with open(file_path, type_write) as f:
        for row in array:
            #la funzione map prende un iterabile e ci applica la funzione
            line = ",".join(map(str, row))
            f.write(line + "\n")

def verifyVector(A):
    dim = A.ndim
    if dim == 1:
        return True
    else:
        return False
