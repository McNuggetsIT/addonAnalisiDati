from moduli.analisi_mono import *
from moduli.multi_dim_operation import *

while True:
    print("\n======MENU======")
    print("1. Analisi array monodimensionali")
    print("2. Analisi array multidimensionali")
    
    scelta = input("Scegli cosa fare [1-2]: ")
    
    
    if scelta == '1':
        arr = np.array([10, 20, 30, 40, 50])
        print("\n======Menu Array monodimensionali======")
        print("1. Statistiche base")
        print("2. Analisi posizionale")
        
        sotto_scelta = input("Cosa scegli[1-2]: ")
    
        if sotto_scelta == '1': 
            print("\n====== Statistiche base ======")
            print("1. Crea array")
            print("2. Gestisci")
            scelta_stat_base = input("Cosa scegli? [1-2]: ")
    
        elif scelta_stat_base == '1':
            stat_base()
        elif scelta_stat_base == '2':
            analis_posizionale()
        else:
            break
    elif scelta == '2':
        
                   
            print("\n======Menu Array multidimensionali======")
            print("1. Prodotto Matrici")
            print("2. Trasposta Matrice")
            print("3. Norma Matrice")
            print("4. Covarianza Matrice")
            print("5. Somma per colonne")
            print("6. Somma per righe")
            print("7. Media per colonne")
            print("8. Media per righe")
                
            scelta_multi_dim = input("Cosa scegli?[1-8]: ")
                
            if scelta_multi_dim == '1':
                prodottoMatrici(matrix)
                 
            elif scelta_multi_dim == '2':
                transpostaMatrice(matrix)
                
            elif scelta_multi_dim == '3':
                normaMatrice(matrix)
                
            elif scelta_multi_dim == '4':
                covarianzaMatrice(matrix)
                    
            elif scelta_multi_dim == '5':
                somma_colonne(matrix)
                    
            elif scelta_multi_dim == '6':
                somma_righe(matrix)
                
            elif scelta_multi_dim == '7':
                media_colonne(matrix)
                    
            elif scelta_multi_dim == '8':
                media_righe(matrix)
            
            else: 
                print("Errore!")
                    
                    
                
                    
                    
                    
                                

        

        