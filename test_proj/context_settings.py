from django.core.urlresolvers import reverse_lazy

__author__ = 'user'


def get_names(request):
    my_menus = {'my_forms_app': reverse_lazy('my_forms_app:name'),
                'app_name': reverse_lazy('app_name:index'),
                'app_adress_book': reverse_lazy('app_adress_book:country'),
                'my_calc': reverse_lazy('my_calc:name'),
                }
    return {'my_menus': my_menus}
