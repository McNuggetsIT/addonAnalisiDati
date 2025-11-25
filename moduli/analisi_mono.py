import numpy as np

def stat_base(arr, file_name="dati.csv"):
    print("1. Minimo nell'array")
    print("2. Massimo nell'array")
    print("3. Media")
    print("4. Deviazione standard")
    
    scelta = input("Scegli cosa fare [1-4]: ")
    
    if scelta == "1":
        ris = np.min(arr)
    elif scelta == "2":
        ris = np.max(arr)
    elif scelta == "3":
        ris = np.mean(arr)
    elif scelta == "4":
        ris = np.std(arr)
    else:
        print("Scelta non valida")
        return None
    
    print("Risultato:", ris)
    
    with open(file_name, "a") as f:
        f.write(f"{scelta},{ris}\n")
    
    return ris


def analis_posizionale(arr, file_name="dati.csv"):
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

    with open(file_name, "a") as f:
        f.write(f"{scelta},{ris}\n")
    
    return ris
