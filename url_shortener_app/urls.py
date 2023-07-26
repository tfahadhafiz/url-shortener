# url_shortener_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect'),
]