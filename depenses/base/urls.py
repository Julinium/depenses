from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('legal/', views.legal, name='legal'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('wip/', views.wip, name='wip'),
    path('report/', views.wip, name='report'),
    path('incomes/', views.wip, name='incomes'),
    path('expenses/', views.expenses, name='expenses'),
    path('expense/<str:pk>', views.expense, name='expense'),
    path('accounts/', views.accounts_list, name='accounts'),
    path('account/details', views.account_form, name='account_details'),
    path('categories/', views.wip, name='categories'),
]
