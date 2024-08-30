from django.contrib import admin
from .models import Airline, Aircraft

# Airline modelini admin paneline ekleme için kullanıldı
@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'callsign', 'founded_year', 'base_airport')  #Görüntülenecek alanlar oluşturuldu
    search_fields = ('name', 'callsign')  # Arama yapabilecek Alanlar oluşturuldu

# Aircraft modelini admin paneline ekleme işlemleri yapıldı
@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('manufacturer_serial_number', 'type', 'model', 'operator_airline')  #Görüntülenecek alanlar oluşturuldu
    search_fields = ('manufacturer_serial_number', 'model')  # Arama yapabilecek Alanlar oluşturuldu
    list_filter = ('operator_airline',)  # Filtreleme yapılabilecek alanlar oluşturuldu
