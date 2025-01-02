from django.shortcuts import render


def about(request):
    templates = 'pages/about.html'
    return render(request, templates)


def rules(request):
    templates = 'pages/rules.html'
    return render(request, templates)
