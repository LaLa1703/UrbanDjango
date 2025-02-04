
from django.shortcuts import render


def platform(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    game = ['Atomic Heart', 'Cyberpunk 2077', 'Payday2']
    return render(request, 'fourth_task/games.html', {'game': game})

def cart(request):
    return render(request, 'fourth_task/cart.html')
