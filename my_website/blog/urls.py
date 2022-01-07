from django.urls import path

from .views import index, all_posts, post_detail

urlpatterns = [
    path("", index, name="index"),
    path("all-posts", all_posts, name="all-posts"),
    path("posts/<slug:slug>", post_detail, name="post-detail")  # posts/my-first-post
]
