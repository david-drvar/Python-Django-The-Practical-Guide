from django.urls import path

import reviews.views

urlpatterns = [
    path("", reviews.views.ReviewView.as_view(), name="index"),
    path("thank-you", reviews.views.ThankYouView.as_view()),
    path("reviews", reviews.views.ReviewsListView.as_view()),
    path("reviews/favorite", reviews.views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", reviews.views.SingleReviewView.as_view()),
]
