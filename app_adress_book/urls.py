from django.conf.urls import url
from . import views
__author__ = 'user'


urlpatterns = [
    url(r'^$', views.CountryView.as_view(), name='country'),
    url(r'^city/(?P<pk>[0-9]+)/$', views.CityView.as_view(), name='city'),
    url(r'^city/adress/(?P<pk>[0-9]+)/$', views.AdressView.as_view(),
        name='adress'),
    url(r'^(?P<pk>[0-9]+)/$', views.PersonView.as_view(),
        name='person'),
    url(r'^city/see_all/(?P<pk>[0-9]+)/$', views.PersonInCityView.as_view(),
        name='person_in_city'),
     url(r'^country/see_all/(?P<pk>[0-9]+)/$',
       views.PersonInCountryView.as_view(), name='person_in_country'),
]
