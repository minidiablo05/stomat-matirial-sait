from django.shortcuts import render


def first_list_educational_materials(request):
    return render(request, 'educational_materials/f_l_e_m.html')

