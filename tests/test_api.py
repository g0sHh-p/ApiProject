import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import current_weather


class TestAPI(unittest.TestCase):
    
    def test_current_weather_with_empty_string(self):
        result = current_weather("")
        assert result is None, "Функция должна вернуть None для пустой строки"
    
    def test_current_weather_with_none(self):
        result = current_weather(None)
        assert result is None, "Функция должна вернуть None для None"
    
    def test_current_weather_with_number(self):
        result = current_weather(123)
        assert result is None, "Функция должна вернуть None для числа"
    
    def test_current_weather_with_valid_city(self):
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        result = current_weather("Москва")
        if result is not None:
            assert isinstance(result, dict), "Результат должен быть словарем"
            if 'data' in result:
                assert isinstance(result['data'], list), "data должен быть списком"
                if result['data']:
                    assert 'city_name' in result['data'][0], "Должно быть поле city_name"


if __name__ == '__main__':
    unittest.main()

