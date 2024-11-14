import sqlite3
import os
from src.classes.Log import Log
log = Log()

class Database:
    def __init__(self, databasePath):
        try:
            log.debug("The '__init__' function of the 'Database' class has been executed.")
            folderPath = os.path.dirname(databasePath)
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
            self.connection = sqlite3.connect(databasePath)
            self.cursor = self.connection.cursor()
            self.storeTableName = "Stores"
            self.createTable()
        except Exception as e:
            log.error(f"Unexpected error occurred in '__init__' function of 'Database' class:\n{e}")

    def createTable(self):
        try:
            log.debug("The 'createTable' function of the 'Database' class has been executed.")
            query = f"""
            CREATE TABLE IF NOT EXISTS {self.storeTableName} (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                StoreId INTEGER NOT NULL,
                StoreName TEXT NOT NULL,
                StoreLink TEXT NOT NULL,
                FollowerCount INTEGER,
                StoreLocation TEXT,
                Categories TEXT
            );
            """
            self.cursor.executescript(query)
            self.connection.commit()
            del query
            return True
        except Exception as e:
            log.error(f"Unexpected error occurred in 'createTable' function of 'Database' class:\n{e}")
            return False

    def createStore(self, storeId:int, storeName:str, storeLink:str, followerCount:int=None, storeLocation:str=None, categories:str=None):
        try:
            log.debug("The 'createStore' function of the 'Database' class has been executed.")
            isAvailable = self.isStoreAvailable(storeId)
            if not isAvailable:
                query = f"INSERT INTO {self.storeTableName} (StoreId, StoreName, StoreLink, FollowerCount, storeLocation, categories) VALUES (?, ?, ?, ?, ?, ?);"
                self.cursor.execute(query, (storeId, storeName, storeLink, followerCount, storeLocation, categories))
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            log.error(f"Unexpected error occurred in 'createStore' function of 'Database' class:\n{e}")
            return False

    def isStoreAvailable(self, storeId:str):
        try:
            log.debug("The 'isStoreAvailable' function of the 'Database' class has been executed.")
            query = f'SELECT StoreId FROM {self.storeTableName} WHERE StoreId = ?;'
            self.cursor.execute(query, (storeId,))
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as e:
            log.error(f"Unexpected error occurred in 'isStoreAvailable' function of 'Database' class:\n{e}")
            return False

    def closeConnection(self):
        try:
            log.debug("The 'closeConnection' function of the 'Database' class has been executed.")
            self.connection.close()
            return True
        except Exception as e:
            log.error(f"Unexpected error occurred in 'closeConnection' function of 'Database' class:\n{e}")
            return False
