from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from advertiser_app.models import (
    Advert,
    Status,
    Category
)
from constants.constants import DEFAULT_STATUS_ID
from advertiser_app.forms import AdvertForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


class AdvertList(ListView):
    template_name = 'adverts/list.html'
    context_object_name = 'adverts'
    model = Advert
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_deleted__exact=False, status__exact=1)
        return queryset


class AdvertForModerationList(AdvertList):
    template_name = 'adverts/moderation_list.html'

    def get_queryset(self):
        queryset = Advert.objects.filter(status__exact=DEFAULT_STATUS_ID, is_deleted__exact=False)
        return queryset


class AdvertDetail(DetailView):
    model = Advert
    template_name = 'adverts/detail.html'


class AdvertDetailModerate(AdvertDetail):
    model = Advert
    template_name = 'adverts/detail.html'


class AdvertCreate(LoginRequiredMixin, CreateView):
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


class AdvertUpdate(UpdateView):
    form_class = AdvertForm
    model = Advert
    template_name = 'adverts/update.html'
    context_object_name = 'advert'

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse('advert_detail_moderate', kwargs={'pk': self.kwargs.get('pk')})
        else:
            return reverse('advert_detail', kwargs={'pk': self.kwargs.get('pk')})


class AdvertDelete(DeleteView):

    def get(self,request, *args, **kwargs):
        ad = Advert.objects.get(id=self.kwargs.get('pk'))
        ad.is_deleted = True
        ad.save()
        return redirect('advert_list')
