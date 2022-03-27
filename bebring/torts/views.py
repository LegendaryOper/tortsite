from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
# Create your views here.


class MainPage(ListView):
    model = Tort
    queryset = Tort.objects.all()
    context_object_name = 'tort'
    paginate_by = 10
    template_name = 'torts/torts_list.html'


class Categories(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'inc/categories_list.html'


class GetTortPage(ListView):
    model = Tort
    context_object_name = 'tort'
    template_name = 'torts/get_tort_page.html'

    def get_queryset(self):
        tort_id = get_object_or_404(Tort, pk=self.kwargs['pk'])
        return tort_id


class GetCategory(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'torts/category_page.html'

    def get_queryset(self):
        return Category.objects.get(pk=self.kwargs['category_pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['torts'] = Tort.objects.filter(category=self.kwargs['category_pk'])
        context['title'] = self.get_queryset().name
        return context







