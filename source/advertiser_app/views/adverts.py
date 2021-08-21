from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from advertiser_app.models import (
    Advert,
    Status,
    Category
)
from django.views.generic.edit import FormMixin
from constants.constants import DEFAULT_STATUS_ID
from advertiser_app.forms import AdvertForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from constants.constants import *
from django.contrib import messages


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


class AdvertDetailModerate(DetailView, FormMixin):
    model = Advert
    form_class = AdvertForm
    template_name = 'adverts/detail.html'

    def post(self, request, *args, **kwargs):
        body = json.loads(self.request.body)
        for key, val in body.items():
            try:
                ad = Advert.objects.get(id=key)
                if val == 'decline':
                    try:
                        ad.status = Status.objects.get(id=DECLINED)
                        ad.save()
                        messages.add_message(
                            request, messages.SUCCESS,
                            f'The advert has been declined.'
                        )
                    except ObjectDoesNotExist:
                        messages.add_message(
                            request,
                            messages.ERROR,
                            f'Something went wrong while moderating. We are working on the problem'
                        )
                else:
                    try:
                        ad.status = Status.objects.get(id=MODERATED)
                        ad.published_at = datetime.now()
                        ad.save()
                        messages.add_message(
                            request, messages.SUCCESS,
                            f'The advert has been approved.'
                        )
                    except ObjectDoesNotExist:
                        messages.add_message(
                            request,
                            messages.ERROR,
                            f'Something went wrong while moderating. We are working on the problem'
                        )
            except ObjectDoesNotExist:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f'Something went wrong while moderating. We are working on the problem'
                )
        return render(request, 'adverts/list.html')


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

    def form_valid(self, form):
        self.object = form.save()
        self.object.status = Status.objects.get(id=DEFAULT_STATUS_ID)
        return super().form_valid(form)

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
