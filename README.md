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



