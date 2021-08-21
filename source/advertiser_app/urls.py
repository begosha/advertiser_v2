from django.urls import path
from advertiser_app.views.adverts import (
    AdvertList,
    AdvertForModerationList,
    AdvertDetail,
    AdvertDetailModerate,
    AdvertCreate,
    AdvertUpdate,
    AdvertDelete
)

urlpatterns = [
    path('', AdvertList.as_view(), name='advert_list'),
    path('moderation/', AdvertForModerationList.as_view(), name='moderation'),
    path('advert/<int:pk>/', AdvertDetail.as_view(), name='advert_detail'),
    path('advert/moderate/<int:pk>/', AdvertDetailModerate.as_view(), name='advert_detail_moderate'),
    path('create/', AdvertCreate.as_view(), name='create'),
    path('update/<int:pk>/', AdvertUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', AdvertDelete.as_view(), name='delete_advert')
]