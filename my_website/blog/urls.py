from django.urls import path

from .views import StartingPageView, AllPostsView, SinglePostView, ReadLaterView

urlpatterns = [
    path("", StartingPageView.as_view(), name="index"),
    path("all-posts", AllPostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>", SinglePostView.as_view(), name="post-detail"),
    path("read-later", ReadLaterView.as_view(), name="read-later")  # posts/my-first-post
]
