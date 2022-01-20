from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     # sorted_posts = sorted(posts, key=get_date)
#     # latest_posts = sorted_posts[-3:]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def all_posts(request):
#     posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": posts
#     })


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    # def get_context_data(self, **kwargs):     I don't need this because I referenced tags directly in post-detail.html
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     return context

# def post_detail(request, slug):
#     # identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     # identified_post = next(post for post in posts if post['slug'] == slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post
#     })
