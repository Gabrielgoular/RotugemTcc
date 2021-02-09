# python
#django
from django.contrib import admin
# project
from .models import Receita, Ingrediente

admin.site.register(Receita)
admin.site.register(Ingrediente)