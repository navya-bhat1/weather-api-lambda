# Weather API using AWS Lambda & API Gateway ☁️

This is a simple AWS Lambda function that fetches current weather data using the OpenWeatherMap API and returns it via an API Gateway endpoint.

---

## 🛠️ Technologies Used

- Python 3.9  
- AWS Lambda  
- AWS API Gateway  
- OpenWeatherMap API  
- GitHub  

---

## 📌 How It Works

1. A user sends a GET request with a `city` query parameter.  
2. The Lambda function calls OpenWeatherMap API with the given city.  
3. It returns temperature, humidity, and weather condition as a JSON response.  

---

## ✅ Sample Output

```json
{
  "city": "mumbai",
  "temperature": 27.99,
  "humidity": 78,
  "condition": "haze"
}
```
---

## 📎 Example URL Usage

[Try the API with Mumbai](https://94tu68abvh.execute-api.us-east-2.amazonaws.com/weather?city=mumbai)
---

## 📝 Note on Weather Data

Weather data may vary slightly depending on the source. This API fetches real-time temperature from OpenWeatherMap, which may differ by 1–2°C from platforms like Google or AccuWeather due to update frequency or data provider differences.

