Overview:
This project is a command-line AI agent powered by Google's Gemini API and OpenWeatherMap. It dynamically responds to user prompts and fetches real-time weather data when asked about the weather in a specific city.
Features:
- Integrates Gemini 1.5 Flash for natural language generation
- Detects weather-related prompts and fetches live data from OpenWeatherMap
- Accepts command-line input and responds intelligently
- Modular design for easy expansion (e.g., news, finance, translation
Technologies Used:
- Python 3
- Google Generative AI (Gemini)
- OpenWeatherMap API
- requests for HTTP calls
- dotenv for secure environment variable management
Setup Instructions:
cd your-repo-name
Install dependencies:
pip install -r requirements.txt
Add your API keys to a .env file:
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
Run the agent:
python main.py "weather in Bengaluru"




