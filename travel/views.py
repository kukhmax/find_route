from django.shortcuts import render

def home(request):
    name = 'Bob'
    context = {
        'name': name,
    }
    return render(request, 'home.html', context=context)

def about(request):
    name = 'About us'
    context = {
        'name': name,
    }
    return render(request, 'about.html', context=context)