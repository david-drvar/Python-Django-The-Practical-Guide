from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        # existing_model = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_model)  INSTANCE IS FOR UPDATING!
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form
        })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(TemplateView):
    template_name = "reviews/reviews_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk = review_id)
        context["review"] = selected_review
        return context
