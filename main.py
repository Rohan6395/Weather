import streamlit as st
import datetime as dt
import requests

# API Details
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# API_KEY = "1d545e8cda8d3ffd2b03964b6e75c091"
API_KEY = "d10f9e96e9cc48bfd6eb4e2ddebb3331"

# Streamlit UI
st.set_page_config(page_title="Weather App", page_icon="☁", layout="centered")
st.title("Weather App")

CITY = st.text_input("Enter City Name:", "Kashipur").strip()

if CITY:
    # Fetch Weather Data
    url = f"{BASE_URL}appid={API_KEY}&q={CITY.replace(' ', '%20')}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") == 200:
        # Extract Data
        temp_celsius = response['main']['temp']
        feels_like_celsius = response['main']['feels_like']
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        description = response['weather'][0]['description'].title()
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        
        col1, col2 = st.columns(2)
        col1.metric("Temperature (℃)", f"{temp_celsius:.2f}")
        col2.metric("Feels Like (℃)", f"{feels_like_celsius:.2f}")
        
        st.write(f"**Weather Description:** {description}")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} m/sec")
        st.write(f"**Sunrise:** {sunrise_time.strftime('%I:%M %p')} local time")
        st.write(f"**Sunset:** {sunset_time.strftime('%I:%M %p')} local time")
        
        st.image("https://source.unsplash.com/600x400/?weather,cloud", use_column_width=True)
    else:
        st.error(f"City not found: {CITY}. Please enter a valid city name.")
    
    # Debugging: Print the response in case of issues
    st.text(f"Debug Info: {response}")


