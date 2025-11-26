import os
import numpy as np
import sqlite3
import csv

#nome db che conterrà il dataset csv
DB_DATASET = "db_california.db"
CALIFORNIA_HOUSING_DATA = "california_housing_data.csv"

#database in output
DB_OUTPUT = "output.db"
if os.path.exists(DB_DATASET):
    os.remove(DB_DATASET)
    
#crea un db con i file nel csv
def csv_to_db():
    conn = sqlite3.connect(DB_DATASET)
    connector = conn.cursor()
            
    connector.execute("""
        CREATE TABLE IF NOT EXISTS output (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        MedInc REAL,
        HouseAge REAL,
        AveRooms REAL,
        AveBedrms REAL,
        Population REAL,
        AveOccup REAL,
        Latitude REAL,
        Longitude REAL,
        MedHouseVal REAL
        );
    """)
            
    with open(CALIFORNIA_HOUSING_DATA, mode="r", encoding="utf-8") as f:
        csv_r = csv.reader(f)
        header = next(csv_r)  # salta intestazione
        print(f"Header rilevato: {header}")
        
        dati_ins = []
        for riga in csv_r:
            MedInc = float(riga[0])
            HouseAge = float(riga[1])
            AveRooms = float(riga[2])
            AveBedrms = float(riga[3])
            Population = float(riga[4])
            AveOccup = float(riga[5])
            Latitude = float(riga[6])
            Longitude = float(riga[7])
            MedHouseVal = float(riga[8])
            
            
            dati_ins.append((MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, MedHouseVal))

        sql_insert = """
            INSERT INTO output (MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, MedHouseVal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        connector.executemany(sql_insert, dati_ins)
        conn.commit()
        print(f"Importati con successo {len(dati_ins)} record.")

    

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
        
def saveFileToDB(array):
    
    conn = sqlite3.connect(DB_OUTPUT)
    cursor = conn.cursor()
    
    sql_create_table = """
        CREATE TABLE IF NOT EXISTS output (
        variable TEXT PRIMARY KEY,
        minimo REAL,
        massimo REAL,
        media REAL,
        stdd REAL,
        );
    """
    
    cursor.execute(sql_create_table)
    print("Tabella creata")
    
    sql_insert = "INSERT INTO output (variabile, minimo, massimo, media, stdd) VALUES (?, ?, ?, ?, ?)"
    
    cursor.executemany(sql_insert, array)
    
    conn.commit()

def verifyVector(A):
    dim = A.ndim
    if dim == 1:
        return True
    else:
        return False
    
csv_to_db()