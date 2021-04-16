from django.shortcuts import render


def sobre_nos(request):
    return render(request, 'sobre_nos/sobre_nos.html', {})
