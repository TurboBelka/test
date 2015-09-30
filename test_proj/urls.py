"""test_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app_name/', include('app_name.urls', namespace="app_name")),
    url(r'app_author/', include('app_author.urls', namespace="app_author")),
    url(r'app_adress_book/country/', include('app_adress_book.urls',
                                     namespace="app_adress_book")),
    url(r'^test_form_app/', include('test_form_app.urls',
                                     namespace="test_form_app")),
    url(r'^test_model_form/', include('test_model_form.urls',
                                     namespace="test_model_form")),
    url(r'^my_forms_app/', include('my_forms_app.urls',
                                     namespace="my_forms_app")),
    url(r'^my_calc/', include('my_calc.urls',
                                     namespace="my_calc")),
]
