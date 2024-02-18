
import requests
def weather_search(city_input,api_key,weather):
    if (weather.json()["cod"]==200):
        condition=(weather.json())["weather"][0]["main"]
        Present_temp=weather.json()["main"]["temp"]
        max_temp=weather.json()["main"]["temp_max"]
        min_temp=weather.json()["main"]["temp_min"]
        print(f"The weather in {city_input} is {condition}.")
        print(f"Temperature :{Present_temp} Max_temp :{max_temp} min_temp :{min_temp}")
    else:
        print("Enter the valid city name")    
city_input=input("Enter the city name :")
api_key="707733af3de329211a3666b6b56f6241"

weather = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}&units=metric")    
weather_search(city_input,api_key,weather)

    
