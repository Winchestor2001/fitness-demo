from django.urls import path
from . import views

urlpatterns = [
    # Выход с аккаунта
    path('logout/', views.logout_page, name='logout'),
    # Страница для Авторизации
    path('login/', views.login_page, name='login'),
    # Страница для Регистрация
    path('registr/', views.registr_page, name='registr'),
    # Страница для Восстановление пароля
    path('reset_password/', views.reset_password_page, name='reset_password'),
    
    # Страница профиля
    path('profile/', views.profile_page, name='profile'),
    
    # Главная страница
    path('', views.home_page, name='home'),
    # Старница программ
    path('programms/', views.programms_page, name='programms'),
    # Страница детали о программе
    path('programm_detail/<int:pk>', views.programm_detail, name='programm_detail'),
    # Страница статьей
    path('articles/', views.articles_page, name='articles'),
    # Страница детали о статье
    path('article_detail/<int:pk>', views.article_detail, name='article_detail'),
    # Страница Избранное
    path('favorites/', views.favorites_page, name='favorites'),
    # Переход на статью/программе через избранное
    path('favorite/<str:slug>', views.favorite_detail, name='favorite'),
    # Проверка избранных програм/статьей
    path('check_favorite/', views.check_favorite, name='check_favorite'),
    

    # Ссылка для чат бота для поиска информацию в базе
    path('search_programm/', views.search_programm, name='search_programm'),
]