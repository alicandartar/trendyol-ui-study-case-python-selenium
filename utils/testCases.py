#Test case bilgileri yer almaktadır.
def test_cases(number):
    return testCases[number]


testCases = [
    # [test case açıklaması, test case önceliği]
    ['Trendyol anasayfasına gidildiğinde sayfanın yüklenmesi gerekir.', 'Kritik'],
    ['Anasayfa giriş butonuna tıklanır, Sıgn In butonunun görülmesi gerekir.', 'Kritik'],
    ['Login sayfasında sisteme kayıtlı kullanıcı ile giriş yapılır, login sonrası anasayfanın yüklenmesi gerekir.', 'Kritik'],
    ['Numaralandırılan tablara sırası ile gidilir, imajların başarılı yüklenildiği görülmelidir.', 'Kritik'],
    ['Rastgele bir butiğe giderek, ürün görsellerinin başarılı olarak yüklenildiği kontrol edilir.', 'Kritik'],
    ['Rastgele gidilen butikte rastgele bir ürünün detayına gidilir, ürün detay sayfasının geldiği görülür.', 'Kritik'],
    ['Ürün detay sayfasında ilgili ürün sepete ekle butonuna tıklanarak sepete eklenir, ürünün sepete eklendiği görülmelidir.', 'Kritik']
]