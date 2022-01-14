from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def all_posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": posts
    })


def post_detail(request, slug):
    # identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    # identified_post = next(post for post in posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
