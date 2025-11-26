import numpy as np
from service import *


def prodottoMatrici(A:np.array, B:np.array,):
    shape_A = np.shape(A)
    shape_B = np.shape(B)
    if shape_A[1] == shape_B[0]:
        output = np.dot(A,B)
        #saveFileToDB(output)
        return output 
    else:
        return False
    
def transpostaMatrice(A:np.array):
    output = np.transpose(A)
    #saveFileToDB(output)
    return output

def normaMatrice(A:np.array):
    output = np.linalg.norm(A)
    #saveFileToDB(output)
    return output


#prende la matrice trasposta
def covarianzaMatrice(At:np.array):
    output = transpostaMatrice(At)
    #saveFileToDB(output)
    return output

    
def somma_colonne(matrix):
    
    sum1 = np.sum(matrix , axis = 0)
    print("Somma per colonne:" , sum1)
    #saveFileToDB(sum1)
    return sum1
    
def somma_righe(matrix):
    sum2 = np.sum(matrix , axis = 1)
    print("Somma per righe:" , sum2)
    #saveFileToDB(sum2)
    return sum2
    
def media_colonne(matrix):
    
    mean1 = np.mean(matrix , axis = 0)
    print("Media per colonne:", mean1)
    #saveFileToDB(mean1)
    return mean1

def media_righe(matrix):

    mean2 = np.mean(matrix, axis = 1)
    print("Media per righe:", mean2)
    #saveFileToDB(mean2)
    return mean2
    
    
    
