from django.urls import path

from recognize_videos.views import (
    RecognizeVideosListView,
    RecognizeVideosArchiveView,
    RecognizeVideosSearchView,
)


urlpatterns = [
    path('', RecognizeVideosListView.as_view(), name='recognize_videos'),
    path('archive/', RecognizeVideosArchiveView.as_view(), name='archive'),
    path('search/', RecognizeVideosSearchView.as_view(), name='search'),
]
