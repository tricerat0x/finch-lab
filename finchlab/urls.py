"""
URL configuration for finchlab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from main_app import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('toys/', ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', ToyCreate.as_view(), name='toys_create'),
]
