from django.urls import path
from django.contrib import admin
from blog import views
from .views import index

urlpatterns = [
    path('',views.index, name='index'),
    # path('',views.index, name='index'),
]
