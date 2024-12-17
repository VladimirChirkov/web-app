from django.shortcuts import render

def gogo(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'hello', '123']
    }
    return render(request, 'main/gogo.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

