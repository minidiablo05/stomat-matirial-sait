from django.urls import path
from educational_materials import views

urlpatterns = [
    path('', views.first_list_educational_materials, name='f_l_e_m'),
    path('anatomia/', views.anatomia, name='anatomia'),
    path('cariesology/', views.cariesology, name='cariesology'),
    path('propaedeutics/', views.propaedeutics, name='propaedeutics'),
    path('surgery/', views.surgery, name='surgery'),
    path('endodontics/', views.endodontics, name='endodontics')
]
