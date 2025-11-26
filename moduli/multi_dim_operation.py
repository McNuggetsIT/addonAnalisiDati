import numpy as np

def prodottoMatrici(A:np.array, B:np.array):
    shape_A = np.shape(A)
    shape_B = np.shape(B)
    if shape_A[1] == shape_B[0]:
        return np.dot(A, B)
    else:
        return False
    
def transpostaMatrice(A:np.array):
    return np.transpose(A)

def normaMatrice(A:np.array):
    return np.linalg.norm(A)

#prende la matrice trasposta
def covarianzaMatrice(At:np.array):
    transpose = transpostaMatrice(At)
    return np.cov(transpose)
    
def somma_colonne(matrix):
    
    sum1 = np.sum(matrix , axis = 0)
    print("Somma per colonne:" , sum1)
    
def somma_righe(matrix):
    sum2 = np.sum(matrix , axis = 1)
    print("Somma per righe:" , sum2)
    
def media_colonne(matrix):
    
    mean1 = np.mean(matrix , axis = 0)
    print("Media per colonne:", mean1)

def media_righe(matrix):

    mean2 = np.mean(matrix, axis = 1)
    print("Media per righe:", mean2)
    
    
    
