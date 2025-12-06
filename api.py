import requests
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")

def current_weather(city : str):
    """
    Получить текущую погоду для указанного города.

    Эта функция делает запрос к Weatherbit API для получения
    текущих погодных данных для заданного города.

    :param city: Название города
    :type city: str
    :return: JSON-ответ от API или None в случае ошибки
    :rtype: dict or None
    :raises requests.exceptions.ConnectionError: При отсутствии интернет-соединения
    :raises requests.exceptions.HTTPError: При ошибках HTTP (4xx, 5xx)
    :raises requests.exceptions.Timeout: При превышении времени ожидания
    :raises ValueError: При ошибках парсинга JSON
    """
    
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
        response.raise_for_status()  # Проверка HTTP статуса
        return response.json()
        
    
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