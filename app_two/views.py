from django.shortcuts import render

def home(request):
    return render(request, 'app_two/home.html')

def page1(request):
    return render(request, 'app_two/page1.html')

def page2(request):
    return render(request, 'app_two/page2.html')
