from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.core, name='core'),
    path('inventory/', views.inventory, name='inventory'),

    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),
    path('info/<int:pk>/', views.info, name='info'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
