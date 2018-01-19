from django.shortcuts import render
import requests

def home(request):
    response = requests.get("https://turismope.herokuapp.com/api/places/pending")
    context = {
        'data': response.json(),
    }
    return render(request, 'home.html', context)
