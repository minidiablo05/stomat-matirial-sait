from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.first_list, name='homepage'),
]
