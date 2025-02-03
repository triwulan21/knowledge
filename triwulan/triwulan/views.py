from django.shortcuts import render

def index(request):
    context = {
        'title': 'Website WND'
    }
    return render(request, 'index.html', context)

def key(request):
    context = {
        'title': 'Badminton Skill'
    }
    return render(request, 'key.html', context)

def masak(request):
    context = {
        'title': 'masak Skill'
    }
    return render(request, 'masak.html', context)

def gitar(request):
    context = {
        'title': 'tamborin Skill'
    }
    return render(request, 'gitar.html', context)

def tenis(request):
    context = {
        'title': 'Tenis meja Skill'
    }
    return render(request, 'tenis.html', context)
