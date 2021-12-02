from django.urls import path
from api.views import TextList

urlpatterns = [
    path('text_list/', TextList.as_view(), name='text_list')
]