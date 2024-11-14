from src.utils.helper import exportDbToExcel
from src.classes.Log import Log # Günlük tutma (Loglama) işlemleri için kullanılan sınıfı içe aktarıyoruz.
log = Log() # Log sınıfını nesne olarak tutar.

def main():
    try:
        log.info("The database is being exported to an Excel file...")
        databasePath = 'src/database/database.db' # SQLite veri tabanı dosyasının yolu
        tableName = 'Stores' # Excel'e aktarılacak tablo ismi
        excelPath = 'Stores.xlsx' # Oluşturulacak Excel dosyasının adı

        exportDbToExcel(databasePath, tableName, excelPath)
        log.info("The database has been successfully exported in Excel format.")
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")
    input("Press 'Enter' to exit...")

if __name__ == "__main__":
    main()