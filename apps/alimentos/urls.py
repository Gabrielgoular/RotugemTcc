# python 
# django
from django.urls import path
# project
from . import views

urlpatterns = [
    path('add/', views.AlimentoCreateView.as_view(), name='alimento__cria'),
    path('<int:pk>/atualizar/', views.AlimentoUpdateView.as_view(), name='alimento__atualiza'),
    path('<int:pk>/excluir/', views.AlimentoDeleteView.as_view(), name='alimento__delete'),
    path('', views.AlimentoListView.as_view(), name='alimento__list'),
    path('<int:pk>/', views.AlimentoDetailView.as_view(), name='alimento__detail'),
]
