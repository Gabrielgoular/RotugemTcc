

#python 
#django
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
#project

class Ingrediente(models.Model):


    receita = models.ForeignKey("receitas.Receita", verbose_name="Receita", on_delete=models.CASCADE)
    alimento = models.ForeignKey("alimentos.Alimento", verbose_name="Alimento", on_delete=models.CASCADE)
    quantidade = models.DecimalField("Quantidade",max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name = "Ingredientes"

    # def __str__(self):
    #         return self.alimento



    def get_u_url(self):
            return reverse("ingrediente__atualiza", kwargs={"pk": self.pk})    

    def get_d_url(self):
            return reverse("ingrediente__delete", kwargs={"pk": self.pk})    





class Receita(models.Model):


    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    nome = models.CharField(max_length=28, verbose_name="Nome")
    quantidade = models.DecimalField("Quantidade", max_digits=10, decimal_places=1)
    descricao = models.CharField(max_length=100, verbose_name="Descrição da receita")
    criado = models.DateTimeField(auto_now_add=True, verbose_name="Criando em")
    ingredientes = models.ManyToManyField("alimentos.Alimento", verbose_name="Ingredientes", through=Ingrediente)
    class Meta:
        verbose_name ='Receita'
        verbose_name_plural ='Receitas'

    def __str__(self):
        return self.nome

    def get_ingredientes(self):
        return  Ingrediente.objects.filter(receita__id=self.pk)

    def get_absolute_url(self):
        return reverse("receita__detail", kwargs={"pk": self.pk})

    def get_add_ingrediente_url(self):
        return reverse("ingrediente__cria", kwargs={"receita": self.pk})


    def get_update_url(self):
        return reverse("receita__atualiza", kwargs={"pk": self.pk})    

    def get_delete_url(self):
        return reverse("receita__delete", kwargs={"pk": self.pk})    
        
    def total_proteina(self):
        total = 0
        for i in self.get_ingredientes():
            total = total + ((float(i.alimento.proteina) * float(i.quantidade)) * float(self.quantidade))
        return total
    
    def total_carbo(self):
        total = 0
        for i in self.get_ingredientes():
            total = total + ((float(i.alimento.carbo) * float(i.quantidade)) * float(self.quantidade))
        return total
    
    def total_gordura(self):
        total = 0
        for i in self.get_ingredientes():
            total = total + ((float(i.alimento.gordura) * float(i.quantidade)) * float(self.quantidade))
        return total
    
    def total_caloria(self):
        total = self.total_gordura()* 9 + self.total_carbo() * 4 + self.total_proteina() * 4
        return total
    
