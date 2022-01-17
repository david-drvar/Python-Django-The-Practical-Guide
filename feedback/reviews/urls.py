from django.urls import path

from reviews.views import index, thank_you

urlpatterns = [
    path("", index, name="index"),
    path("thank-you", thank_you)
]
