from django.urls import path
from . import views

urlpatterns = [
    #path('', views.dashboard, name='dashboard'),
    path('materiels/', views.materiels_list, name='materiels'),
    path('materiels/<int:id>/', views.materiel_detail, name='materiel_detail'),
    path('materiels/ajouter/', views.ajouter_materiel, name='ajouter_materiel'),
]