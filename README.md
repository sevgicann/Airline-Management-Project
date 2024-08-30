Proje Özeti:

Proje Adı: Airline Project
Proje Tanımı: Havayolları ve onlara bağlı uçakların eklenebildiği, değiştirilebildiği ve listelenebildiği bir tasarım oluşturma.

Kullanılan Teknolojiler: Django, Visual Studio Code, JWT, Postman

Proje Fonksiyonları: Kullanıcı Doğrulama ve Yetkinlendirme: JWT Authentication
API İşlevi: Uçakların ve havayollarının eklenebildiği, listelenebilindiği, değiştirilebildiği ve silindiği bir uygulama oluşturma.

Test Aşaması:

Postman Testleri: Postman’da proje gereksinimlerine uygun testler gerçekleştirildi.
Alınan Hatalar: Access token’a erişimde hata alındı. TokenObtainPairView class’ı kullanarak JWT token’lara erişim hatası düzeltildi. 

Sonuç:
Projede istenilen uçak ekleme, listeleme ve değiştirme kısımları sorunsuz olarak çalışmaktadır. 
Havayolları kısmı gereksinimlere göre eklenip, listelenip, değiştirilebilmektedir. 
Sisteme erişimi olan kullanıcılar ve kullanıcı grupları Authentication and Authorization başlığı altında görüntülenebilmektedir. 
Panel içerisindeki search kısımları düzgün bir şekilde çalışmaktadır.
