from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, FormView, CreateView
from django.shortcuts import get_object_or_404
from .forms import *
# Create your views here.


class MainPage(ListView):
    model = Tort
    queryset = Tort.objects.all()
    context_object_name = 'torts'
    paginate_by = 9
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
    template_name = 'torts/torts_list.html'

    def get_queryset(self):
        return Category.objects.get(pk=self.kwargs['category_pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['torts'] = Tort.objects.filter(category=self.kwargs['category_pk'])
        context['title'] = self.get_queryset().name
        return context


class OfferFormView(CreateView):
    template_name = 'torts/make_offer.html'
    form_class = OfferForm
    success_url = '/'


    def form_valid(self, form):
        print('form')
        if form.is_valid():
            form.instance.status = StatusForOffer.objects.get(pk=1)
            form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('invalid')
        print(form)
        return super().form_invalid(form)