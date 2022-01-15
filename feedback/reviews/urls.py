from django.urls import path

from reviews.views import index

urlpatterns = [
    path("", index, name="index")
]
