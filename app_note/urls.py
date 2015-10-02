from django.conf.urls import url
from app_note.views import get_note

urlpatterns = [
    url(r'^$', get_note, name='note'),
    ]
