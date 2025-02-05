from django.shortcuts import render, redirect
from .forms import UserRegister

# Имитация базы данных пользователей
users = ['admin', 'user123', 'test_user']


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Валидация данных
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif not age.isdigit() or int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            return render(request, 'fifth_task/success.html', {'username': username})

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            # Дополнительная валидация
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                return render(request, 'fifth_task/success.html', {'username': username})
        else:
            info['error'] = 'Проверьте введенные данные'

    info['form'] = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)