from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from django.core import serializers


# Выход с аккаунта
def logout_page(request):
    logout(request)
    return redirect('home')


# Рендер Страницу для Авторизации
def login_page(request):
    context = {'login': 'active'}
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        usr = authenticate(username=email, email=email, password=pwd)
        if usr:
            login(request, usr)
            return redirect('/')
        else:
            context['message'] = 'Ошибка. Почта или пароль не верный'
            context['col'] = 'danger'
    return render(request, 'login.html', context)


# Рендер Страница для Регистрация
def registr_page(request):
    context = {'registr': 'active'}
    if request.method == 'POST':
        ism = request.POST['fname']
        familya = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        usr = User.objects.filter(email=email)
        if len(password) < 8:
            context['message'] = 'Длинна пароля должна быть 8 символов'
            context['col'] = 'danger'
        elif usr:
            context['message'] = 'Ошибка. Такой пользователь уже есть'
            context['col'] = 'danger'
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = ism
            user.last_name = familya
            user.save()
            return redirect('login')
    return render(request, 'registration.html', context)


# Рендер Страница для Восстановление пароля
def reset_password_page(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['password1']
        usr = User.objects.filter(email=email)
        if pwd != pwd1:
            context['message'] = 'Пароль не совпадает'
            context['col'] = 'danger'
        elif not usr:
            context['message'] = 'Ошибка. Такой пользователь не зарегистрирован'
            context['col'] = 'danger'
        else:
            user = User.objects.get(username=email, email=email)
            user.set_password(pwd)
            user.save()
            return redirect('login')

    return render(request, 'reset_password.html', context)


# Рендер Страница профиля
def profile_page(request):
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        item = request.POST
        user.email = item['email']
        user.first_name = item['fname']
        user.last_name = item['lname']
        if request.FILES:
            file_obj = request.FILES['avatar']
            filename = f'avatar/{request.user}_{file_obj}'
            with default_storage.open(filename, 'wb+') as d:
                for chunk in file_obj.chunks():
                    d.write(chunk)
            user.avatar = filename
        user.save()

    context = {'user': user}
    return render(request, 'profile.html', context)


# Рендер Главная страница
def home_page(request):
    info = SiteInfo.objects.all()
    context = {'home': 'active', 'info': info[0]}
    return render(request, 'home.html', context)


# Рендер Старница программ
def programms_page(request):
    programms = FitnessProgramm.objects.all()
    context = {'programms_status': 'active', 'programms': programms}
    return render(request, 'programms.html', context)


# Рендер Страница детали о программе
def programm_detail(request, pk):
    programm = FitnessProgramm.objects.get(pk=pk)
    check_favorite = ''
    if not request.user.is_anonymous:
        check_favorite = Favorite.objects.filter(favorite_slug=programm.slug, user=request.user)
    status = 'fa-solid' if len(check_favorite) != 0 else 'fa-regular'
    context = {'programms_status': 'active', 'programm': programm, 'status': status}
    return render(request, 'programm_detail.html', context)


# Рендер Страница статьей
def articles_page(request):
    articles = Article.objects.all()
    context = {'articles_status': 'active', 'articles': articles}
    return render(request, 'articles.html', context)


# Рендер Страница детали о статье
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    check_favorite = ''
    if not request.user.is_anonymous:
        check_favorite = Favorite.objects.filter(favorite_slug=article.slug, user=request.user)
    status = 'fa-solid' if len(check_favorite) != 0 else 'fa-regular'
    context = {'articles_status': 'active', 'article': article, 'status': status}
    return render(request, 'article_detail.html', context)


# Рендер Страница Избранное
def favorites_page(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {'favorites_status': 'active', 'favorites': favorites}
    return render(request, 'favorites.html', context)


# Рендер Переход на статью/программе через избранное
def favorite_detail(request, slug):
    check_favorite = Favorite.objects.filter(favorite_slug=slug, user=request.user)
    status = 'fa-solid' if len(check_favorite) != 0 else 'fa-regular'
    try:
        programm = FitnessProgramm.objects.get(slug=slug)
        context = {'programm': programm, 'status': status}
        return render(request, 'programm_detail.html', context)
    except:
        article = Article.objects.get(slug=slug)
        context = {'article': article, 'status': status}
        return render(request, 'article_detail.html', context)


# Проверка избранных програм/статьей
def check_favorite(request):
    data = request.GET
    if data['status'] == 'false':
        Favorite.objects.create(
            user=request.user,
            favorite_title=data['title'],
            favorite_slug=data['slug'],
        )
    else:
        Favorite.objects.get(favorite_slug=data['slug']).delete()

    return HttpResponse('true')


# Ссылка для чат бота для поиска информацию в базе
def search_programm(request):
    data = request.GET
    new_data = []
    for i in data:
        new_data.append(str(data[i].strip()))
    print(new_data)
    # programms = FitnessProgramm.objects.filter(intensity=new_data[0], type=new_data[1], gender=new_data[2], part_of_body=new_data[3])
    programms = FitnessProgramm.objects.filter(intensity=new_data[0]).filter(type=new_data[1]).filter(gender=new_data[2]).filter(part_of_body=new_data[3])
    print(programms)
    data = serializers.serialize('json', programms)
    return HttpResponse(data, content_type="application/json")


