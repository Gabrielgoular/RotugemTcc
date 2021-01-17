# python 
# django
from django.urls import path
# project
from . import views

urlpatterns = [
    path('add/', views.ReceitaCreateView.as_view(), name='receita__cria'),
    path('<int:pk>/atualizar/', views.ReceitaUpdateView.as_view(), name='receita__atualiza'),
    path('<int:pk>/excluir/', views.ReceitaDeleteView.as_view(), name='receita__delete'),
    path('', views.ReceitaListView.as_view(), name='receita__list'),
    path('<int:pk>/', views.ReceitaDetailView.as_view(), name='receita__detail'),
    path('ingredientes/add/<int:receita>/', views.IngredienteCreateView.as_view(), name='ingrediente__cria'),
    path('ingredientes/<int:pk>/atualizar/', views.IngredienteUpdateView.as_view(), name='ingrediente__atualiza'),
    path('ingredientes/<int:pk>/excluir/', views.IngredienteDeleteView.as_view(), name='ingrediente__delete'),

]
