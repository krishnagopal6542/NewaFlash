from django.shortcuts import render
from news.models import newsData,City
import requests
from .forms import CityForm


# Create your views here.

def news_flash(request):

    news = newsData.objects.all()

    # form = CityForm()

    url ='http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=9624fe578105ee772952e983f24723c7'
    # city = 'Las Vegas'
    # city_weather = requests.get(url.format(city)).json()
    # print(city_weather)

    cities = City.objects.all() 
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)

        


    # if request.method == 'POST': # only true if form is submitted
    #     form = CityForm(request.POST) # add actual request data to form for processing
    #     form.save() # will validate and save if validate
    # form = CityForm()
 
    print(weather_data)

    context = {'weather' : weather_data}


    # return render(request, "news_flash.html",context) 


    return render(request, "news_flash.html",{'news':news}) 