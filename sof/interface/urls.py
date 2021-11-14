from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='Farmfully-home'),
    path('forums/', views.forums,name='Forums'),
    path('predict/', views.predict,name='Predict-Disease'),
    path('predict-result/', views.predict_process,name='Predict-Disease-Result'),
    path('learning/', views.learning,name='E-learning'),
]
