import tkinter as tk
import requests

api_key = "ae7db23517d06326f286b18aeefa31c3"
base_url = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(location):
    params = {"q": location, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if 'name' in weather_data:
        location_label.config(text=f"Location: {weather_data['name']}")
    else:
        location_label.config(text="Location: City not found")

    temp_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
    humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    weather_label.config(text=f"Weather Conditions: {weather_data['weather'][0]['description']}")

def get_weather_info():
    location = location_entry.get()
    weather_data = get_weather(location)
    display_weather(weather_data)

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Increase the size of the window
window.geometry('400x300')  # Set width to 400 pixels and height to 300 pixels

# Create labels and entry fields
location_label = tk.Label(window, text="Enter a city or ZIP code:")
location_label.pack()

location_entry = tk.Entry(window)
location_entry.pack()

temp_label = tk.Label(window, text="")
temp_label.pack()

humidity_label = tk.Label(window, text="")
humidity_label.pack()

weather_label = tk.Label(window, text="")
weather_label.pack()

# Create a button to get weather information
submit_button = tk.Button(window, text="Get Weather", command=get_weather_info)
submit_button.pack()

# Run the Tkinter main loop
window.mainloop()
