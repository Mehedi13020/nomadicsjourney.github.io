from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("memories", views.memories, name='memories'),
    path("contact", views.contact, name='contact'),
    path("journey", views.journey, name='journey'),
    
]
