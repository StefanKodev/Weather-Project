from django.shortcuts import render
import requests


def home(request):
    city_weather = None

    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        api_key = '0bea6ab1ab03451986c03403233008'
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}'

        response = requests.get(url)
        data = response.json()

        temperature = data['current']['temp_c']
        conditions = data['current']['condition']['text']

        city_weather = {
            'name': city_name,
            'temperature': temperature,
            'conditions': conditions,
        }

    context = {'city_weather': city_weather}
    return render(request, 'weather/home.html', context)
