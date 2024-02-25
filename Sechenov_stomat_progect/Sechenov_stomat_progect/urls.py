from django.urls import path
from django.urls import include
from homepage import views
 
urlpatterns = [
    path('', include('homepage.urls')),
]