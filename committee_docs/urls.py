from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents_list, name='documents'),
    #path('documents/', views.documents_list, name='documents')
]
