from django.urls import path
from advertiser_app.views.adverts import (
    AdvertList
)

urlpatterns = [
    path('', AdvertList.as_view(), name='advert_list'),
]