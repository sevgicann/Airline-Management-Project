# Airline Project

## Proje Tanımı
Airline Project, havayolları ve onlara bağlı uçakların eklenebildiği, değiştirilebildiği ve listelenebildiği bir uygulama tasarımıdır. Proje, kullanıcı doğrulama ve yetkilendirme ile birlikte API işlevselliği sunar.

## Kullanılan Teknolojiler
- **Django:** Web uygulaması geliştirme için kullanılan framework.
- **Visual Studio Code:** Kodlama ve geliştirme ortamı.
- **JWT (JSON Web Tokens):** Kullanıcı doğrulama ve yetkilendirme için.
- **Postman:** API testleri için.

## Proje Fonksiyonları
- **Kullanıcı Doğrulama ve Yetkilendirme:** JWT Authentication ile kullanıcı doğrulama ve yetkilendirme sağlanır.
- **API İşlevi:** Uçakların ve havayollarının eklenebildiği, listelenebildiği, değiştirilebildiği ve silinebileceği bir API uygulaması oluşturulmuştur.

## Test Aşaması
- **Postman Testleri:** Proje gereksinimlerine uygun testler gerçekleştirilmiştir.
- **Alınan Hatalar:** Access token’a erişimde hata alınmış, `TokenObtainPairView` sınıfı kullanılarak JWT token’lara erişim hatası düzeltilmiştir.

## Sonuç
Projede istenilen uçak ekleme, listeleme ve değiştirme işlemleri sorunsuz bir şekilde çalışmaktadır. Havayolları kısmı gereksinimlere uygun olarak eklenip, listelenip, değiştirilebilmektedir. Sisteme erişimi olan kullanıcılar ve kullanıcı grupları Authentication ve Authorization başlığı altında görüntülenebilmektedir. Panel içerisindeki arama işlevleri düzgün bir şekilde çalışmaktadır. Postman üzerinden gerekli sorgulamalar yapıldı.
- Obtain Authentication Token
- Create an Airline
- Update an Airline
- Retrieve an Airline
- List All Airlines
- Create an Aircraft
- Update an Aircraft
- Retrieve an Aircraft
- Delete an Aircraft
- Delete an Airline

  Medium Link: https://medium.com/@sevgicann.kilic


