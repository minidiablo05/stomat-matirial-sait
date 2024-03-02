from django.shortcuts import render


def first_list_educational_materials(request):
    return render(request, 'educational_materials/f_l_e_m.html')

def anatomia(request):
    return render(request, 'educational_materials/anatomia.html')

def cariesology(request):
    return render(request, 'educational_materials/cariesology.html')

def propaedeutics(request):
    return render(request, 'educational_materials/propaedeutics.html')

def surgery(request):
    return render(request, 'educational_materials/surgery.html')

def endodontics(request):
    return render(request, 'educational_materials/endodontics.html')
