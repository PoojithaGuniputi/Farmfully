from django.urls import path
from . import views

urlpatterns = [
    path('', views.fertiforms,name='Fertilizer'),
    path('result/', views.addDetails,name='Fertilizer-Result'),
]
