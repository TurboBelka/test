from django.forms import ModelForm
from .models import AuthorTest, ArticleTest


class AuthorForm(ModelForm):
    class Meta:
        model = AuthorTest
        fields = ['first_name', 'last_name', 'birth_date']


class ArticleForm(ModelForm):
    class Meta:
        model = ArticleTest
        fields = ['pub_date', 'headline', 'content', 'reporter']
