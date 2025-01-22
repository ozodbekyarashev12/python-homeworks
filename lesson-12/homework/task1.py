import requests

# Define your API key (replace YOUR_API_KEY with your actual API key)
api_key = "YOUR_API_KEY"

# Define the city for which you want to get weather data
city = "Tashkent"

# Construct the API URL to fetch the weather data for the city
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send the GET request to the OpenWeatherMap API
response = requests.get(url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    
    # Extract relevant information from the response data
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    
    # Print the results
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Pressure: {pressure} hPa")
else:
    # If the request was not successful, print the error code and message
    print(f"Error fetching weather data. HTTP Status Code: {response.status_code}")
    print(response.json())
