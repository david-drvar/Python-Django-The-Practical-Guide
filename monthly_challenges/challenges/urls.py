from django.urls import path

from challenges.views import monthly_challenge_by_number, monthly_challenge, index

urlpatterns = [
    path("", index),
    path("<int:month>", monthly_challenge_by_number),
    path("<str:month>", monthly_challenge, name="month-challenge"),
]
