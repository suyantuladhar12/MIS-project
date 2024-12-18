Project 1. OpenWeatherMap
Fetch Data Using an API
1.	Write a Python script to fetch recent weather data for your city using the OpenWeatherMap API.
	- Use the API endpoint: https://api.openweathermap.org/data/2.5/weather
	- Parameters: q=<city_name>, appid=<api_key>.
	- Display the temperature, humidity, and weather description.
2.	Modify your script to accept the city name as user input.
3.	Save the results (city name, temperature, and weather description) into a CSV file using the pandas library.

Project 2. NewsData
Fetch News Articles and Analyze Sentiment
1.	Use the NewsData.io API to fetch the latest news headlines for a specific country (e.g., NP for Nepal).
	- API endpoint: https://newsdata.io/api/1/latest
	- Parameters: country=<country_code>, apikey=<api_key>.
2.	Extract the title and description fields from the response.
3.	Use NLTK's SentimentIntensityAnalyzer to calculate sentiment scores for each headline and classify the overall sentiment as "Positive", "Negative", 	or "Neutral".
4.	Save the results (title, description, sentiment scores, sentiment label) to a JSON file.

Project 3. Kalimati
Fetch Kalimati Vegitables Rates
1.	Use the KalimatiBazar-API to fetch the latest exchange rates.
2.	Extract exchange rates for the KalimatiBazar Vegetable Rates.
3.	Write the exchange rates into a CSV file with appropriate headers.