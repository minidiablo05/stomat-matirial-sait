from django.urls import path
from educational_materials import views
 
urlpatterns = [
    path('', views.first_list_educational_materials, name='f_l_e_m'),
]
