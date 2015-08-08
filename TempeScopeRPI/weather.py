import openweathermapy.core as owm

location = "Oregon,OH"
settings = {"units": "imperial", "lang": "EN"}

views = {
"summary": ["main.temp", "main.pressure", "main.humidity", "wind.speed",
"clouds.all"]
}
# add rain.3h
data = owm.get_current(location, **settings)
print(data.get_dict(views["summary"]))
