from django.shortcuts import render


# Create your views here.
def get_note(request):
    return render(request, 'app_note/index.html', {'title': "app_note"})
