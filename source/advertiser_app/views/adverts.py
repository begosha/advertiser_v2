from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from advertiser_app.models import (
    Advert,
    Status,
    Category
)
from constants.constants import DEFAULT_STATUS_ID
from advertiser_app.forms import AdvertForm

class AdvertList(ListView):
    template_name = 'adverts/list.html'
    context_object_name = 'adverts'
    model = Advert
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset().filter(status__exact=1)
        return queryset


class AdvertForModerationList(AdvertList):
    template_name = 'adverts/moderation_list.html'

    def get_queryset(self):
        queryset = Advert.objects.filter(status__exact=DEFAULT_STATUS_ID)
        return queryset


class AdvertDetail(DetailView):
    model = Advert
    template_name = 'adverts/detail.html'


class AdvertDetailModerate(AdvertDetail):
    model = Advert
    template_name = 'adverts/detail.html'


class AdvertCreate(CreateView):
    template_name = 'adverts/create.html'
    form_class = AdvertForm
    model = Advert

    def form_valid(self, form):
        author = self.request.user
        advert = form.save(commit=False)
        advert.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('advert_list')

