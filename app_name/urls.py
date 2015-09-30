from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
__author__ = 'user'


urlpatterns = [
    # ex: /app_name/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /app_name/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /app_name/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(),
        name='results'),
    # ex: /app_name/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
  #  static(settings.STATIC_URL),
]
