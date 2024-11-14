# Trendyol Store Scraper

## Projenin Amacı
Bu proje, Trendyol platformundaki tüm mağaza bilgilerini toplamak için geliştirilmiştir.

## Nasıl Çalıştırılır?
1. **Python Yüklü Sistemler İçin**  
   Python bilgisayarınızda yüklü ise, öncelikle `requirements.txt` dosyasındaki bağımlılıkları yüklemeniz gerekmektedir. Kurulum işlemini tamamladıktan sonra `main.py` dosyasını çalıştırarak yazılımı başlatabilirsiniz.
   
2. **Python Yüklü Olmayan Sistemler İçin**  
   Python yüklü değilse, doğrudan `main.exe` uygulamasını çalıştırarak programı başlatabilirsiniz.

3. **Program Çalıştırma Adımları**  
   Program başlatıldığında, bir konsol penceresi açılacaktır. Konsolda, başlangıç ve bitiş değerlerini girmeniz istenecektir.  
   - **Başlangıç Değeri:** Kaç numaralı mağazadan veri toplamaya başlanacağını belirler.  
   - **Bitiş Değeri:** Kaçıncı mağazada işlemin sona ereceğini belirtir.  
   Eğer programı ilk kez çalıştırıyorsanız, başlangıç değeri olarak `0` girin ve bitiş değerini boş bırakıp Enter tuşuna basarak devam edin.

## Mağaza Bilgileri Nereye Kaydedilir?
Toplanan mağaza bilgileri, `src/database/` klasöründe oluşturulan `database.db` isimli SQLite dosyasına kaydedilmektedir. Eğer mağaza zaten veri tabanında mevcutsa, tekrar eklenmez.

## Mağaza Verilerini Excel Dosyasına Aktarma
Mağaza verilerini Excel formatına dönüştürmek için `dbToExcel.py` Python dosyasını veya `dbToExcel.exe` uygulamasını çalıştırabilirsiniz. Uygulama çalıştırıldığında, mevcut dizinde bir Excel dosyası oluşturulacaktır.

## Program Aynı Anda Birden Fazla Kez Çalıştırılabilir mi?
Eğer mağaza bilgilerini hızlıca toplamak istiyorsanız programı birden fazla kez çalıştırmak isteyebilirsiniz. Ancak, bu durumda Trendyol'a aynı anda daha fazla istek gönderileceği için IP adresiniz geçici olarak engellenebilir. Bu nedenle programı eşzamanlı olarak birden fazla kez çalıştırmanız önerilmez. Eğer bu işlemi yapmak isterseniz, farklı IP adresleri üzerinden çalıştırmayı düşünebilirsiniz.

## Ek Bilgiler
- **Veritabanı Yedekleme:** Düzenli aralıklarla `database.db` dosyasını yedeklemeyi unutmayın. Böylece kazıdığınız verileri tekrar toplamak zorunda kalmazsınız.
- **Loglama:** Proje içinde hata takibi için loglama yapılmıştır. Bir sorunla karşılaşmanız halinde, yazılımcıya yardımcı olması için `logs` klasörünü paylaşabilirsiniz.
- **Hata Giderme:** Eğer loglar sorunu çözmede yeterli olmazsa, komut satırından (CMD) uygulamayı başlatarak, hata mesajlarını konsolda görüntüleyebilir ve yazılımcıya iletebilirsiniz.