from django.contrib import admin
from django.urls import path, include
from .views import greetings_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple_route/', greetings_func, name='simple-route'),
    path('auth/',  include(('home.rest_urls', 'home'), namespace='auth')),
    path('books/',  include(('books.rest_urls', 'books'), namespace='books')),
    path('moviepy/',  include(('video_generation.rest_urls', 'video_generation'), namespace='moviepy')),
]
