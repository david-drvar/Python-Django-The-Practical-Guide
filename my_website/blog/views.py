from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import CommentForm
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


class SinglePostView(View):
    def get(self, request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "form" : CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  #bind comment with post because it is missing in form
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

        context = {
            "post": post,
            "form" : comment_form
        }
        return render(request, "blog/post-detail.html", context)


# def post_detail(request, slug):
#     # identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     # identified_post = next(post for post in posts if post['slug'] == slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post
#     })
