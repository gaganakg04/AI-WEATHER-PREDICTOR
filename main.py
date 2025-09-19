import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv
import requests

def main():
    load_dotenv()
    api_key=os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model=genai.GenerativeModel("gemini-1.5-flash-002")
    def get_weather(city):
        apikey = "c7d89a7f5fb1caa561f08f94253fe654"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
        response = requests.get(url)
        data = response.json()
        return f"{city} weather: {data['weather'][0]['description']}, {data['main']['temp']}°C"
    if(len(sys.argv) < 2):
        print("Need a prompt argument")
        sys.exit(1)
    else:
        for i in range(1, len(sys.argv)):
            Prompt= str(sys.argv[i])
            if "weather" in Prompt.lower():
                city = Prompt.split("in")[-1].strip()
                print(f"Extracted city: {city}")
                weather_info = get_weather(city)
                Prompt += f"\n{weather_info}"
            response = model.generate_content(Prompt)
            print(response.text)
            
main()