# python 
# django
from django import forms
# project
from .models import Receita, Ingrediente

class ReceitaForm(forms.ModelForm):

    class Meta:
        model = Receita
        fields = [
            'nome', 
            'quantidade',
            'descricao', 
            
        ]

        
class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = [
        
            'alimento', 
            'quantidade',
            
            
        ]