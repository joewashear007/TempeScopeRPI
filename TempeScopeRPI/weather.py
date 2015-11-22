from pyowm import OWM

#variables
# ---------------------------------------
location = "Oregon,OH"
api_key = "00cf720f141fb21188ddf5d69f2db8d1"

# code 
# -----------------------------------------

def GetWeather():
    owm = OWM(api_key)
    obs = owm.weather_at_place(location)  
    w = obs.get_weather()
    weather = {}
    weather['clouds'] = w.get_clouds()
    weather['rain'] = w.get_rain()
    weather['wind'] = w.get_wind()
    weather['humidity'] = w.get_humidity()
    weather['temp'] = w.get_temperature('fahrenheit')
    print(weather)
    return weather
