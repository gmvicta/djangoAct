from django.shortcuts import render

def home(request):
    return render(request, 'app_one/home.html')

def page1(request):
    return render(request, 'app_one/page1.html')

def page2(request):
    return render(request, 'app_one/page2.html')
