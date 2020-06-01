from django.urls import path
from core.spot import views

urlpatterns = [
    path('', views.index, name='index'),

]
