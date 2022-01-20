from django.urls import path

from .views import StartingPageView, AllPostsView, SinglePostView

urlpatterns = [
    path("", StartingPageView.as_view(), name="index"),
    path("all-posts", AllPostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>", SinglePostView.as_view(), name="post-detail")  # posts/my-first-post
]
