from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy 
from django.contrib.messages.views import SuccessMessageMixin
from . import models


class RecipeListView(ListView):
  model = models.Recipe
  template_name = 'recipes/home.html'
  context_object_name = 'recipes'

def recipes_home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        recipe=recipe.objects.filter(title__icontains=q)
    else:
        recipe=recipe.objects.all()
...
from django.views.generic import ListView, DetailView
...
class RecipeDetailView(DetailView):
  model = models.Recipe

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models

class RecipeListView(ListView):
  model = models.Recipe
  template_name = 'recipes/home.html'
  context_object_name = 'recipes'

class RecipeDetailView(DetailView):
  model = models.Recipe

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  success_url = reverse_lazy('recipes-home')

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
  model = models.Recipe
  fields = ['title', 'ingredientes' , 'description', 'categoria', ]

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class RecipeUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Recipe
  fields = ['title', 'ingredientes' , 'description', 'categoria', ]
  success_url: reverse_lazy ('recipes/home.html')
  successe_message = 'Receta cambiada exitosamente!'

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)