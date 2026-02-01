from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store_View, name='store')
]
