from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'title': 'Главная'}
    return render(request, 'index.html', context=context)


def catalog(request):
    context = {'title': 'Каталог'}
    return render(request, 'catalog.html', context=context)
