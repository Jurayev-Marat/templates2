from django.urls import path
from . import views

urlpatterns = [
    # ✅ ASOSIY SAHIFALAR
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('design/', views.design, name='design'),
    path('company/', views.company, name='company'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),

    # ✅ AUTH SAHIFALARI
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),

    # ✅ DASHBOARD SAHIFALARI
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
]