# python
# django
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Project
from .models import Receita, Ingrediente
from .forms import ReceitaForm, IngredienteForm




class ReceitaCreateView( LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'receitas/receita_form.html'
    model = Receita
    form_class = ReceitaForm
    success_message = 'Receita adicionado com sucesso!'

    def form_valid(self, form):
        receita = form.save(commit=False)
        receita.usuario = self.request.user
        receita.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(receita.get_absolute_url())
    


class ReceitaUpdateView( LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'receitas/receita_form.html'
    model = Receita
    form_class = ReceitaForm
    success_message = 'Receita atualizado com sucesso!'
  

class ReceitaListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Receita
    template_name = 'receitas/receita_list.html'


class ReceitaDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Receita
    template_name = 'receitas/receita_detail.html'


class ReceitaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'receitas/receita_delete.html'
    model = Receita
    success_url = reverse_lazy('receita__list')
    success_message = 'Receita excluido com sucesso!'

   


class IngredienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'receitas/ingrediente_form.html'
    model = Ingrediente
    form_class = IngredienteForm
    success_message = 'Ingrediente adicionado com sucesso!'

    def form_valid(self, form):
        ingrediente = form.save(commit=False)
        receita = Receita.objects.get(id=self.kwargs["receita"])
        ingrediente.receita = receita
        ingrediente.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(receita.get_absolute_url())


class IngredienteUpdateView( LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'receitas/Ingrediente_form.html'
    model = Ingrediente
    form_class = IngredienteForm
    success_message = 'Ingrediente atualizado com sucesso!'


    def form_valid(self, form):
        ingrediente = form.save(commit=False)
        receita = ingrediente.receita
        ingrediente.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(receita.get_absolute_url())


  

class IngredienteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'receitas/ingrediente_delete.html'
    model = Ingrediente
    success_url = reverse_lazy('receita__list')
    success_message = 'Ingrediente excluido com sucesso!'


    

    