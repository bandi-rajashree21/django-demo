from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "Walk for 20min",
    "march": "Learn Django daily",
    "april": "Read 10 pages of a book",
    "may": "Practice coding for 1 hour",
    "june": "Drink 3 liters of water daily",
    "july": "Wake up at 5 AM",
    "august": "Exercise for 30 minutes",
    "september": "Meditate for 15 minutes",
    "october": "Avoid sugar",
    "november": "Write a journal daily",
    "december": "Reflect on the year and plan ahead",
}

def monthly_challenge_by_numbers(request,month):
    months=list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    forward_month=months[month-1]
    redirect_path=reverse ("month-challenge",args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("This month not supported")
