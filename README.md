# Ödül Avı Oyunu
Bu proje, Python dersi ödevi kapsamında geliştirilmiş basit bir şans oyunudur. 
Ödevde istenen "kullanıcıdan veriyi komut satırı (terminal) dışında farklı bir arayüzden alma ve çıktı verme" şartını sağlamak amacıyla, arayüz tasarımı için Python'un dahili kütüphanesi olan Tkinter kullanılmıştır.

# Oyunun Mantığı
- Program, 0 ile 9 arasında rastgele bir sayıyı "ödül" olarak belirler.
- Kullanıcının ödülü bulmak için toplam 3 deneme hakkı vardır.
- Kullanıcı tahminini arayüzdeki metin kutusuna girer.
- Geçersiz bir karakter (harf, boşluk vb.) girilirse program çökmek yerine hata mesajı verir.
- 3 hak bittiğinde veya ödül bulunduğunda oyun sona erer. "Yeniden Oyna" butonu ile değerler sıfırlanarak tekrar oynanabilir.

# Kullanılan Araçlar
- **Python 3:** Temel programlama dili.
- **Tkinter:** Grafik kullanıcı arayüzü (GUI) oluşturmak ve veri giriş/çıkışını sağlamak için.
- **Random kütüphanesi:** Ödülün yerini rastgele belirlemek için.

# Nasıl Çalıştırılır?
Projeyi çalıştırmak için bilgisayarınızda Python'un kurulu olması yeterlidir (Tkinter, Python ile birlikte otomatik gelir). 
Kodu indirdikten sonra terminal veya komut istemcisine aşağıdaki komutu yazarak oyunu başlatabilirsiniz:

python oyun.py
