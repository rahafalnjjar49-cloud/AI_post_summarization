from django.urls import path
from rest_framework import routers

from .views.generate import generate_post
from .views import get_posts
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('posts/get_post',get_posts, name='get_post'),
    path('post/generate',generate_post, name='generate_post'),
]
urlpatterns += router.urls

