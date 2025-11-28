import requests
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")

def current_weather(city : str):
    
    try:
        
        if not api_key:
            print("API ключ не найден")
            return None
        
        
        if not city or not isinstance(city, str):
            print("Некорректное название города")
            return None
        
        params = {
            "key": api_key,
            "lang": "ru",
            "city": city,
        }
        
        response = requests.get("https://api.weatherbit.io/v2.0/current", params=params, timeout=10)
        return response
        
    
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения к интернету")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ошибка: {e}")
        return None
    
    except requests.exceptions.Timeout:
        print("Превышено время ожидания")
        return None
    
    except ValueError as e:
        print(f"Ошибка при обработке JSON ответа: {str(e)}")
        return None
    
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
        return None