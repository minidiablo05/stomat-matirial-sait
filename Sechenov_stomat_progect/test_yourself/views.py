from django.shortcuts import render


def test_yourself(request):
    return render(request, 'test_yourself/test_yourself.html')
