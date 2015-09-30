from django.views import generic
from .models import Country, City, Adress, Person


# Create your views here.
class CountryView(generic.ListView):
    template_name = 'apps/country.html'
    context_object_name = 'country_list'
    model = Country

    def get_context_data(self, **kwargs):
        context = super(CountryView, self).get_context_data(**kwargs)
        context['title'] = "app_adress_book"
        return context


class CityView(generic.ListView):
    template_name = 'apps/city.html'
    context_object_name = 'city_list'

    def get_queryset(self):
        country_id = self.kwargs['pk']
        return City.objects.filter(country__id=country_id)

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['title'] = "app_adress_book"
        return context


class AdressView(generic.ListView):
    template_name = 'apps/adress.html'
    context_object_name = 'adress_list'
    model = Adress

    def get_queryset(self):
        city_id = self.kwargs['pk']
        return Adress.objects.filter(city__id=city_id)

    def get_context_data(self, **kwargs):
        context = super(AdressView, self).get_context_data(**kwargs)
        context['title'] = "app_adress_book"
        return context


class PersonView(generic.ListView):
    template_name = 'apps/person.html'
    context_object_name = 'person_list'
    model = Person

    def get_queryset(self):
        adress_id = self.kwargs['pk']
        return Person.objects.filter(adress__id=adress_id)

    def get_context_data(self, **kwargs):
        context = super(PersonView, self).get_context_data(**kwargs)
        context['title'] = "app_adress_book"
        return context


class PersonInCityView(generic.ListView):
    template_name = 'apps/all_person_city.html'
    context_object_name = 'person_list'
    model = Person

    def get_queryset(self):
        city_id = self.kwargs['pk']
        return Person.objects.filter(adress__city__id=city_id)

    def get_context_data(self, **kwargs):
        context = super(PersonInCityView, self).get_context_data(**kwargs)
        context['title'] = "app_adress_book"
        return context


class PersonInCountryView(generic.ListView):
    template_name = 'apps/all_person_country.html'
    context_object_name = 'person_list'
    model = Person

    def get_queryset(self):
        country_id = self.kwargs['pk']
        return Person.objects.filter(adress__city__country__id=country_id)

    def get_context_data(self, **kwargs):
        context = super(PersonInCountryView, self).get_context_data(**kwargs)
        context['title'] = "app_adress_book"
        return context
