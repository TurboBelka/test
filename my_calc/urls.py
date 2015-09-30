from django.conf.urls import url
from my_calc.views import get_name

urlpatterns = [
    url(r'^$', get_name, name='name'),
    ]
