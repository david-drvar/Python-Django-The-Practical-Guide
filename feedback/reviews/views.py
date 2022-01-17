from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.views import View

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


def thank_you(request):
    return render(request, "reviews/thank_you.html")
