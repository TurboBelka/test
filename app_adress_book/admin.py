from django.contrib import admin
from .models import Country, City, Adress, Person


class CountryAdmin(admin.ModelAdmin):
    model = Country


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_id', 'city_name')


class AdressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_id', 'adress')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_birth')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Adress, AdressAdmin)
admin.site.register(Person, PersonAdmin)
