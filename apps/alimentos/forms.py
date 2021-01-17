# python 
# django
from django import forms
# project
from .models import Alimento

class AlimentoForm(forms.ModelForm):

    class Meta:
        model = Alimento
        fields = [
            'nome',
            'proteina', 
            'carbo',
            'gordura', 
            'sodio', 
            'fibra', 
            'polisaturado',
            'poliInsaturado', 
            'monosaturado',
            'monoinsaturado',
        ]