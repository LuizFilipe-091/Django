from django.urls import path
from .views import all_posts

urlpatterns = [
    path('', all_posts, name='all_posts'),
]