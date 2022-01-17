from django.urls import path

import reviews.views
from reviews.views import thank_you

urlpatterns = [
    path("", reviews.views.ReviewView.as_view(), name="index"),
    path("thank-you", thank_you)
]
