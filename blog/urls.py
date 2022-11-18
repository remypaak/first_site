from django.urls import path, include
from blog import views


urlpatterns = [
    path("", views.index, name="index-page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:post_name>", views.specific_post, name="post_detail-pages")
]