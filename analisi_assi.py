import numpy as np

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
    
    
    