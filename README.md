# trendyol-ui-study-case-python-selenium

Python Selenium modülü ile geliştirildi.

## Proje Yapısı : Page Object Model

## Pages
### Base Page 

BasePage class basit fonksiyonları içerir.
### Other Pages
Her sayfa için class yapısı oluşturuldu. POM 

## Utils

### Locators

Web elementlerinin bakımını kolaylaştırmak için locators altında web elementler toplandı.

### TestCases

- Trendyol anasayfasına gidildiğinde sayfanın yüklenmesi gerekir.
- Anasayfa giriş butonuna tıklanır, Sıgn In butonunun görülmesi gerekir.
- Login sayfasında sisteme kayıtlı kullanıcı ile giriş yapılır, login sonrası anasayfanın yüklenmesi gerekir.
- Numaralandırılan tablara sırası ile gidilir, imajların başarılı yüklenildiği görülmelidir.
- Rastgele bir butiğe giderek, ürün görsellerinin başarılı olarak yüklenildiği kontrol edilir.
- Rastgele gidilen butikte rastgele bir ürünün detayına gidilir, ürün detay sayfasının geldiği görülür.
- Ürün detay sayfasında ilgili ürün sepete ekle butonuna tıklanarak sepete eklenir, ürünün sepete eklendiği görülmelidir.

## Çalıştırmak için
```bash
python3 -m unittest tests.test_master
```
