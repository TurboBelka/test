from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic
from .forms import AuthorForm, ArticleForm
from .models import AuthorTest, ArticleTest
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy


class MyMixinClass(object):
    def get_context_data(self, **kwargs):
        print 123
        context = super(MyMixinClass, self).get_context_data(**kwargs)
        context['title'] = "my_forms_app"
        return context


def delete_all_article(request):
    ArticleTest.objects.all().delete()
    return HttpResponseRedirect(reverse('my_forms_app:list_articles'))


def get_name(request):
    formset_cls = modelformset_factory(AuthorTest, form=AuthorForm, extra=3)
    if request.method == 'POST':
        formset = formset_cls(request.POST)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(reverse('my_forms_app:list_authors_view'))
    else:
        formset = formset_cls()
    return render(request, 'author_form.html', {'formset': formset,
                                                'title': "my_forms_app"})


class AuthorsListView(MyMixinClass, generic.ListView):
    template_name = 'app/list_authors.html'
    context_object_name = 'author_list'
    model = AuthorTest


class ArticleView(MyMixinClass, generic.FormView):
    template_name = 'app/add_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('my_forms_app:list_articles')

    def form_valid(self, form):
        form.save()
        return super(ArticleView, self).form_valid(form)


class ArticleListView(MyMixinClass, generic.ListView):
    template_name = 'app/list_articles.html'
    context_object_name = 'article_list'
    model = ArticleTest


class ArticleDelete(MyMixinClass, generic.DeleteView):
    template_name = 'app/articletest_confirm_delete.html'
    model = ArticleTest
    success_url = reverse_lazy('my_forms_app:list_articles')

