from src.classes.Trendyol import Trendyol # Trendyol'dan veri kazıma işlemini sağlayacak sınıfı içe aktarıyoruz.
from src.utils.helper import clear
from src.classes.Database import Database # Veri tabanı işlemleri için kullanılan sınıfı içe aktarıyoruz.
from src.classes.Log import Log # Günlük tutma (Loglama) işlemleri için kullanılan sınıfı içe aktarıyoruz.

log = Log() # Log sınıfını nesne olarak tutar.

def getFirstLastNumbers():
    """Kullanıcıdan başlangıç ve bitiş mağaza numaralarını alır."""
    while True:
        try:
            firstId = int(input("Başlangıç Mağaza ID Değeri (İlk defa çalıştırıyorsanız 0 girin): "))
            if firstId < 0:
                print("Başlangıç değeri negatif olamaz.")
                continue
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        lastIdInput = input("Son Mağaza ID Değeri (Sonsuz döngü için boş bırakın): ")
        
        if lastIdInput:
            try:
                lastId = int(lastIdInput)
                if lastId <= firstId:
                    print("Son ID, başlangıç ID'sinden büyük olmalıdır.")
                    continue
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
                continue
        else:
            lastId = None # Sonsuz döngü için None
            
        return firstId, lastId

def main():
    """ Ana fonksiyondur. """
    try:
        database = Database("src/database/database.db") # Verilerin kaydedilmesi için bir veri tabanı oluşturur.
        trendyol = Trendyol() # Trendyol'dan veri kazımak için gerekli sınıfı nesne olarak tutuyoruz.
        storeId, lastId = getFirstLastNumbers() # Kullanıcıdan, taranacak mağaza ID'leri için başlangıç ve bitiş değerlerini girmesini ister.
        log.info(f"Başlangıç ID'si: {storeId}, Bitiş ID'si: {lastId}")
        
        while True:
            if lastId != None and storeId > lastId: # Eğer son ID değeri mevcut ise, son ID'ye ulaşıldığında program sonlandırılır.
                break

            if storeId % 200 == 0: # Her hedef sorguda bir konsolu temizler.
                clear()

            isStoreAvailable = trendyol.isStoreAvailable(storeId) # Mağaza ID'sine göre mağazanın mevcut olup olmadığını kontrol eder.
            if isStoreAvailable == True: # Eğer mağaza mevcut ise bilgilerini alır ve veri tabanına kaydeder.
                print(f"[{storeId}] Mağaza mevcut.")
                storeName = trendyol.getStoreName(storeId)
                storeLink = f"https://trendyol.com/magaza/magaza-m-{storeId}?sk=1"
                followerCount = trendyol.getFollowerCount(storeId)
                categories = trendyol.getCategories(storeId)
                categories = ', '.join(categories)
                storeLocation = trendyol.getStoreLocation(storeId)

                if storeName: # Mağazanın mevcutluğunu, isim kontrolü yaparak doğruluyoruz.
                    database.createStore(storeId, storeName, storeLink, followerCount, storeLocation, categories)
                    print(f"[{storeId}] | Mağaza İsmi: {storeName} | Takipçi Sayısı: {followerCount} | Konum: {storeLocation} | Kategoriler: {categories}")
                else:
                    print(f"[{storeId}] Mağazanın bilgileri alınamadı.")
            else: # Mağaza mevcut değilse koşul sağlanır.
                print(f"[{storeId}] Mağaza mevcut değil.")

            storeId += 1 # Bir sonraki mağazaya geçer.
        
        log.debug("All stores have been scanned.")
        input("Press 'Enter' to exit...")
    except Exception as e:
        log.error(f"Unexpected error in 'main' function:\n{e}")
    finally:
        database.closeConnection() # Veri tabanı bağlantısını sonlandırır.

if __name__ == "__main__":
    main()