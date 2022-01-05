from django.urls import path

from .views import monthly_challenges

urlpatterns = [
    path("<month>", monthly_challenges)
]
