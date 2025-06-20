# 🌤️ Weather API using AWS Lambda & API Gateway

This is a simple AWS Lambda function that fetches current weather data using the OpenWeatherMap API and returns it via an API Gateway endpoint.

---

## 🛠️ Technologies Used
- Python 3.9
- AWS Lambda
- AWS API Gateway
- OpenWeatherMap API
- GitHub

---

## 🚀 How It Works

1. A user sends a GET request with a `city` query parameter.
2. The Lambda function calls the OpenWeatherMap API using the provided city.
3. It returns temperature, humidity, and weather condition as a JSON response.

---

## ✅ Sample Output

```json
{
  "city": "your_city_name",
  "temperature": 28.05,
  "humidity": 61,
  "condition": "clear sky"
}
