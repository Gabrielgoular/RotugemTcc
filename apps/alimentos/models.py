
#python 
#django
from django.urls import reverse
from django.db import models
#project

class Alimento(models.Model):
    nome = models.CharField(max_length=254, verbose_name="Nome")
    proteina = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Proteinas G:")
    carbo = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Carboidratos G:")
    gordura = models.DecimalField(max_digits=10, decimal_places=2,verbose_name= "Gordura G:")   
    sodio = models.DecimalField( max_digits=10, decimal_places=2, verbose_name="Sódio G:")    
    fibra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fibras G:")    
    polisaturado = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Polisaturado G:", blank=True, null= True, default=None )       
    poliInsaturado = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Poli-Insaturado G:", blank=True, null=True, default=None ) 
    monosaturado = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Monosaturado G:", blank=True, null=True, default=None)
    monoinsaturado = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Mono-Insaturado G:", blank=True, null=True, default=None)

    class Meta:
        verbose_name ='Alimento'
        verbose_name_plural ='Alimentos'

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse("alimento__detail", kwargs={"pk": self.pk})


    def get_update_url(self):
        return reverse("alimento__atualiza", kwargs={"pk": self.pk})    

    def get_delete_url(self):
        return reverse("alimento__delete", kwargs={"pk": self.pk})    