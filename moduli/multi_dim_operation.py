import numpy as np

def prodottoMatrici(A:np.array, B:np.array):
    shape_A = np.shape(A)
    shape_B = np.shape(B)
    if shape_A[1] == shape_B[0]:
        return np.dot(A, B)
    else:
        return False
    
def transpostaMatrice(A):
    return np.transpose(A)

def normaMatrice(A):
    return np.linalg.norm(A)

#prende la matrice trasposta
def covarianzaMatrice(At):
    transpose = transpostaMatrice(At)
    return np.cov(transpose)
