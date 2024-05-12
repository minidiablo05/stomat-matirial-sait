from django.urls import path
from test_yourself import views

urlpatterns = [
    path('', views.test_yourself, name='test'),
]
