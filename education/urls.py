from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gestion_scolarite', views.gestion_scolarite, name='gestion_scolarite'),

]