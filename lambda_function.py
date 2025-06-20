import json
import urllib.request

def lambda_handler(event, context):
    api_key = "e9d3ab49065d347e21d9b4a3fd9a0ca9"
    
    # Get city from query string parameters
    city = event.get("queryStringParameters", {}).get("city", "bangalore")  # Default: bangalore
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        with urllib.request.urlopen(url) as response:
            weather_data = json.loads(response.read().decode('utf-8'))

        humidity = weather_data['main']['humidity']
        temperature = weather_data['main']['temp']
        condition = weather_data['weather'][0]['description']

        return {
            'statusCode': 200,
            'body': json.dumps({
                'city': city,
                'temperature': temperature,
                'humidity': humidity,
                'condition': condition
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    
