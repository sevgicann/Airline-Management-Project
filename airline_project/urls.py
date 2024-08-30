
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   
    path('api/', include('airlines.urls')),  # API endpointleri için kullanıldı
     path('', admin.site.urls),  # Boş URL'yi admin paneline yönlendirme için kullanıldı
    
]
