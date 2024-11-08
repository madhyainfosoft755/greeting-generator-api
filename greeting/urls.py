
from django.contrib import admin
from django.urls import path

from greeting import views

urlpatterns = [
    path('', views.user_login, name="login"), 
    path('dashboard/', views.dashboard),
    path('billing/', views.billing),
    path('generate-greeting/', views.generate_greeting, name="generate-greeting"),
    path('user-dashboard/', views.user_dashboard, name="user-dashboard"),
    path('admin-dashboard/', views.admin_dashboard, name="admin-dashboard"),
    path('clients/', views.admin_clients,name="clients"),
    path('occasions/', views.admin_occasions,name="occasions"),   
    path('add-client/', views.add_new_client, name='add-client'),
    path('card/', views.card_view, name='card_view'),
    path('greeting-templates/', views.greeting_templates, name='greeting_templates'),
    path('logout/', views.logout_view, name='logout'),
]


