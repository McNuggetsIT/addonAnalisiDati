from moduli.analisi_mono import stat_base, analis_posizionale
from moduli.multi_dim_operation import *
from moduli.service import readFileToArray

while True:
    print("\n======MENU======")
    print("1. Analisi array monodimensionali")
    print("2. Analisi array multidimensionali")
    print("0. Uscire")
    
    scelta = input("Scegli cosa fare [0-2]: ")
    
    if scelta == '1':
        print("\n======Menu Array monodimensionali======")
        print("1. Statistiche base")
        print("2. Analisi posizionale")
        
        sotto_scelta = input("Cosa scegli [1-2]: ")
        arr = readFileToArray("analisi.csv")
        
        if sotto_scelta == '1': 
            stat_base(arr)
        elif sotto_scelta == '2':
            analis_posizionale(arr)
        else:
            print("Scelta non valida")
            
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
            prodottoMatrici()
        elif scelta_multi_dim == '2':
            transpostaMatrice()
        elif scelta_multi_dim == '3':
            normaMatrice()
        elif scelta_multi_dim == '4':
            covarianzaMatrice()
        elif scelta_multi_dim == '5':
            somma_colonne()
        elif scelta_multi_dim == '6':
            somma_righe()
        elif scelta_multi_dim == '7':
            media_colonne()
        elif scelta_multi_dim == '8':
            media_righe()
        else: 
            print("Errore!")
            
    elif scelta == '0':
        print("Uscita dal programma...")
        break
    else:
        print("Scelta non valida")
