import tkinter as tk
import requests
import time

# Create your views here.
def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=8366743f315fb1134da860e4cc7703e0"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] *1.8 - 459.67)
    temp_min = int(json_data['main']['temp_min'] *1.8 - 459.67)
    temp_max = int(json_data['main']['temp_max'] *1.8 - 459.67)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S AM", time.gmtime(json_data['sys']['sunrise'] - 28800))
    sunset = time.strftime("%I:%M:%S PM", time.gmtime(json_data['sys']['sunset'] - 28800))

    final_info = condition + "\n" + str(temp) + "°F"
    final_data = "\n" + "Temp Max: " + str(temp_max) + "\n" + "Temp Min: " + str(temp_min) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset + "\n"
    label1.config(text = final_info)
    label2.config(text = final_data)
   
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")



f = ("poppins", 20, "bold")
t = ("poppins", 25, "bold")

textfield = tk.Entry(canvas, justify = 'center', font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(canvas, font = f)
label1.pack()
label2 = tk.Label(canvas, font = t)
label2.pack()


canvas.mainloop()