# Create your views here.
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Eat no meat for the entire month!",
    "september": "Walk for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Eat no meat for the entire month!",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    if month > len(monthly_challenges):
        return HttpResponseNotFound("Invalid month")
    forward_month = list(monthly_challenges.keys())[month - 1]
    redirect_path = reverse("month-challenge", args=[forward_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
