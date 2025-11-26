import numpy as np
from moduli.service import saveFileToCSV, readFileToArray

def stat_base(arr, file_name="output.csv"):
    
    print("Scegli la colonna da analizzare:")
    print("0. MedInc")
    print("1. HouseAge")
    print("2. AveRooms")
    print("3. AveBedrms")
    print("4. Population")
    print("5. AveOccup")
    print("6. Latitude")
    print("7. Longitude")
    print("8. MedHouseVal")
    
    col = int(input("Indice colonna [0-8]: "))
    colonna = arr[:,col]
    
    print("1. Minimo nell'array")
    print("2. Massimo nell'array")
    print("3. Media")
    print("4. Deviazione standard")
    
    scelta = input("Scegli cosa fare [1-4]: ")
    
    if scelta == "1":
        ris = np.min(colonna)
    elif scelta == "2":
        ris = np.max(colonna)
    elif scelta == "3":
        ris = np.mean(colonna)
    elif scelta == "4":
        ris = np.std(colonna)
    else:
        print("Scelta non valida")
        return None
    
    print("Risultato:", ris)
    saveFileToCSV(file_name, np.array([ris]))


def analis_posizionale(arr, file_name="output.csv"):
    print("1. Indice del minimo")
    print("2. Indice del massimo")
    print("3. Mediana")
    print("4. Posizione ordinata di inserimento")
    
    scelta = input("Scegli cosa fare [1-4]: ")
    
    if scelta == "1":
        ris = np.argmin(arr)
    elif scelta == "2":
        ris = np.argmax(arr)
    elif scelta == "3":
        ris = np.median(arr)
    elif scelta == "4":
        x = float(input("Scrivi il valore da inserire: "))
        ris = np.searchsorted(np.sort(arr), x)
    else:
        print("Scelta non valida")
        return None
    
    print("Risultato:", ris)
    saveFileToCSV(file_name, np.array([ris]))
    
def calc_stats(arr):
    n_col = ["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","MedHouseVal"]
    
    ris= []
    for i,nome in n_col:
        col = arr[:, i]
        minimo = np.min(col)
        massimo = np.max(col)
        media = np.mean(col)
        stdd = np.std(col)
        ris.append((nome,minimo,massimo,media,stdd))
    return ris
        
