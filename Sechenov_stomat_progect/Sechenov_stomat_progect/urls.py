from django.urls import path
from django.urls import include


urlpatterns = [
    path('', include('homepage.urls')),
    path('educational_materials/', include('educational_materials.urls')),
    path('test/', include('test_yourself.urls')),
    path('contact/', include('contact.urls')),
]
