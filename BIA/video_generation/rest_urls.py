from django.urls import path
import video_generation.rest_views as rest_views

urlpatterns = [
    path('video_gen/', rest_views.VideoGenerationView.as_view(), name='video-gen'),
]