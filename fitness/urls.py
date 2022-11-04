from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_page, name='logout'),
    path('login/', views.login_page, name='login'),
    path('registr/', views.registr_page, name='registr'),
    path('reset_password/', views.reset_password_page, name='reset_password'),
    
    path('', views.home_page, name='home'),
    path('programms/', views.programms_page, name='programms'),
    path('programm_detail/<int:pk>', views.programm_detail, name='programm_detail'),
    path('articles/', views.articles_page, name='articles'),
    path('article_detail/<int:pk>', views.article_detail, name='article_detail'),
    path('favorites/', views.favorites_page, name='favorites'),
    path('favorite/<str:slug>', views.favorite_detail, name='favorite'),
    path('check_favorite/', views.check_favorite, name='check_favorite'),
]