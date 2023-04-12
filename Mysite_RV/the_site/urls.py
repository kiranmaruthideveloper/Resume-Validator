from django.urls import path
from . import views

urlpatterns = [
    path('', views.the_site, name='the_site'),
]

