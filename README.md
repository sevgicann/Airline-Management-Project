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
- Obtain Authentication Token: http://127.0.0.1:8000/api/test-token/
- Create an Airline: http://127.0.0.1:8000/api/airline/
- Update an Airline: http://127.0.0.1:8000/api/airline/9/
- Retrieve an Airline: http://127.0.0.1:8000/api/airline/9/
- List All Airlines: http://127.0.0.1:8000/api/airline/
- Create an Aircraft: http://127.0.0.1:8000/api/aircraft/
- Update an Aircraft: http://127.0.0.1:8000/api/aircraft/9/
- Retrieve an Aircraft: http://127.0.0.1:8000/api/aircraft/9/
- Delete an Aircraft: http://127.0.0.1:8000/api/aircraft/delete/
- Delete an Airline: http://127.0.0.1:8000/api/airline/delete/


