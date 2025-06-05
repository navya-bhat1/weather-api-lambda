import json
import requests

def lambda_handler(event, context):
    api_key = "e9d3ab49065d347e21d9b4a3fd9a0ca9"
    
    try:
        city = event['queryStringParameters']['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            condition = data['weather'][0]['description']
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'city': city,
                    'temperature': temperature,
                    'humidity': humidity,
                    'condition': condition
                })
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({"error": data.get("message", "Unknown error")})
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
