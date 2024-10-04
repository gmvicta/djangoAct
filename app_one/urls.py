from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_one_home'),
    path('page1/', views.page1, name='app_one_page1'),
    path('page2/', views.page2, name='app_one_page2'),
]
