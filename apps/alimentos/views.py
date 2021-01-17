# python
# django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# project
from ..receitas.models import Receita
from .models import Alimento
from .forms import AlimentoForm

class AlimentoCreateView( LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'alimentos/alimento_form.html'
    model = Alimento
    form_class = AlimentoForm
    success_message = 'Alimento adicionado com sucesso!'
    


class AlimentoUpdateView( LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'alimentos/alimento_form.html'
    model = Alimento
    form_class = AlimentoForm
    success_message = 'Alimento atualizado com sucesso!'
  

class AlimentoListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Alimento
    template_name = 'alimentos/alimento_list.html'


class AlimentoDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Alimento
    template_name = 'alimentos/alimento_detail.html'

    def get_context_data(self, object):
        context = super().get_context_data()
        context['receitas'] = self.object.receita_set.all()
        return context


class AlimentoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'alimentos/alimento_delete.html'
    model = Alimento
    success_url = reverse_lazy('alimento__list')
    success_message = 'Alimento excluido com sucesso!'

    

    