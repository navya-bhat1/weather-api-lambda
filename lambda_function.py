import json
import urllib.request

def lambda_handler(event, context):
    try:
        city = event.get("queryStringParameters", {}).get("city", "mumbai")
        api_key = "e9d3ab49065d347e21d9b4a3fd9a0ca9"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"]
        }

        return {
            'statusCode': 200,
            'body': json.dumps(weather_info)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
