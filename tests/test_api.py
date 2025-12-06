import unittest
import os
import requests
from weather.api import current_weather


class SimpleWeatherTests(unittest.TestCase):
    

    def test_invalid_inputs(self):
        
        test_cases = [
            "",           
            None,         
            123,          
            [],           
        ]
        
        for city in test_cases:
            with self.subTest(city=city):
                try:
                    result = current_weather(city)
                   
                    self.assertTrue(True)
                except Exception as e:
                    self.fail(f"Функция не обработала некорректный ввод {city}: {e}")

    def test_without_api_key(self):
        """Тест когда API_KEY не установлен"""
        original_key = os.getenv("API_KEY")
        
        
        if "API_KEY" in os.environ:
            del os.environ["API_KEY"]
        
        try:
            
            result = current_weather("Москва")
            self.assertTrue(True)
        finally:
           
            if original_key:
                os.environ["API_KEY"] = original_key

    def test_real_api_call(self):
        
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        try:
            
            test_response = requests.get("https://api.weatherbit.io/v2.0/current", timeout=5)
        except requests.exceptions.ConnectionError:
            self.skipTest("Нет подключения к интернету")
        
        
        try:
            result = current_weather("Москва")
            self.assertTrue(True)  
        except Exception as e:
            self.fail(f"Реальный вызов API вызвал ошибку: {e}")
    
    def test_valid_city_name(self):
        
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        result = current_weather("Москва")
        
        self.assertIsNotNone(result or None)  


if __name__ == '__main__':
    unittest.main()


