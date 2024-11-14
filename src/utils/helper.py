import json # Json formatında işlemler gerçekleştirebilmek için kullanılır.
import os # İşletim sistemi (Operating System) işlemleri için kullanılır.
import pandas # Veri işlemleri için kullanılır.
import sqlite3 # SQLite veri tabanı işlemleri için kullanılır.

def getConfig() -> dict:
    """ Konfigürasyon dosya içeriğini Json formatında okur ve sözlük olarak döndürür. """
    with open("config.json", 'r', encoding='utf-8') as file:
        configDict = json.load(file)
    return configDict

def removeSuffix(text, suffix) -> str:
    """ Bir metnin sonundaki istenilen yazıyı çıkarır. """
    if text.endswith(suffix):
        return text[:len(text) - len(suffix)].strip()
    return text

def clear():
    """ Konsolu temizler. """
    if os.name == 'nt': # İşletim sistemi Windows ise koşul sağlanır.
        os.system('cls') # CMD'nin 'cls' komutu ile konsol temizlenir.
    else: # İşletim sistemi Windows değil ise koşul sağlanır.
        os.system('clear') # Terminal'in 'clear' komutu ile konsol temizlenir.

def exportDbToExcel(databasePath: str, tableName: str, excelPath: str):
    try:
        connection = sqlite3.connect(databasePath) # Veri tabanına bağlanır.
        query = f"SELECT * FROM {tableName};" # Veri tabanındaki bütün verileri çekecek sorguyu yazar.
        dataFrame = pandas.read_sql_query(query, connection) # Veriyi pandas DataFrame'e aktarır.
        dataFrame.to_excel(excelPath, index=False, engine='openpyxl') # DataFrame'i Excel dosyasına yazar.
        connection.close() # Veri tabanı bağlantısını sonlandırır.
    except Exception as e:
        print(f"Unexpected error in 'exportDbToExcel' function: {e}")