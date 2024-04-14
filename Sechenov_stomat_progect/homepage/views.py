from django.shortcuts import render


def first_list(request):
    return render(request, 'homepage/first_list.html')
