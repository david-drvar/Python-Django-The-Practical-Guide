from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView

from reviews.forms import ReviewForm
from reviews.models import Review


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#
#         return render(request, "reviews/review.html", {
#             "form": form
#         })
#
#     def post(self, request):
#         # existing_model = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_model)  INSTANCE IS FOR UPDATING!
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # context_object_name = "review"   not needed because django uses model name automatically
