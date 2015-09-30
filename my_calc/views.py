from django.shortcuts import render


# Create your views here.
def get_name(request):
    return render(request, 'index.html', {'title': "my_calc"})
