# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": "Learn Django for at least 20 minutes every day!",
}


def index(request):
    alternative = """<ul>
                    <li><a href="january">January</a></li>
                    <li>February</li>
                    <li>March</li>
                    </ul>"""

    response_data = "<ul>"
    months = list(monthly_challenges.keys())
    for month in months:
        path = reverse("month-challenge", args=[month])
        response_data += f"<li><a href=\"{path}\">{month.capitalize()}</li>"
    response_data += "</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    if month > len(monthly_challenges):
        return HttpResponseNotFound("Invalid month")
    forward_month = list(monthly_challenges.keys())[month - 1]
    redirect_path = reverse("month-challenge", args=[forward_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
