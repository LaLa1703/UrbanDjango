
from django.shortcuts import render  # type: ignore


def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    items = {'1': 'Игра The Witcher 3 - 1999 руб.',
             '2': 'Игра Cyberpunk 2077 - 2499 руб.',
             '3': 'Игра Red Dead Redemption 2 - 2999 руб.'}
    return render(request, 'third_task/games.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
