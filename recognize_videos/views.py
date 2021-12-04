from django.shortcuts import render
from django.views import View

from recognize_videos.models import RecognizeVideo


class RecognizeVideosListView(View):
    def get(self, request):
        context = {
            'recognize_videos': RecognizeVideo.objects.all()[:3],
            'recognize_videos_dict': {video.pk: video.transcript for video in RecognizeVideo.objects.all()[:3]},
            'main': True,
        }
        return render(request, 'recognize_videos/list_recognize_videos.html', context=context)


class RecognizeVideosArchiveView(View):
    def get(self, request):
        context = {
            'archive_recognize_videos': RecognizeVideo.objects.all(),
            'archive': True,
        }
        return render(request, 'recognize_videos/archive_recognize_videos.html', context=context)


class RecognizeVideosSearchView(View):
    def get(self, request):
        search = request.GET.get('search')

        if search:
            search = search.strip()
            result = RecognizeVideo.objects.filter(transcript__icontains=search)
            return render(request, 'recognize_videos/search_recognize_videos.html', {'search_recognize_videos': result, 'search': True})

        return render(request, 'recognize_videos/search_recognize_videos.html', {'search': True})
