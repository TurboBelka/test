from django.conf.urls import url
from .views import get_name, AuthorsListView, ArticleView, ArticleListView
from .views import ArticleDelete, delete_all_article

urlpatterns = [
    url(r'^$', get_name, name='name'),
    url(r'^list_authors', AuthorsListView.as_view(), name='list_authors_view'),
    url(r'^add_article', ArticleView.as_view(), name='add_article'),
    url(r'^list_articles', ArticleListView.as_view(), name='list_articles'),
    url(r'^delete_article/(?P<pk>[0-9]+)/', ArticleDelete.as_view(),
        name='delete_article'),
    url(r'^delete_all_article', delete_all_article, name='delete_all'),
    ]