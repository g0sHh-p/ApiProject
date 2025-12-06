import unittest
import json
import os
from weather.save import save_json, save_txt


class TestWeatherFunctionsSimple(unittest.TestCase):


    def test_save_json(self):
        """Простой тест для save_json"""
        test_data = {
            'city_name': 'Тестовый город',
            'temp': 20,
            'app_temp': 22,
            'weather': {'description': 'облачно'},
            'rh': 50,
            'pres': 1000,
            'wind_spd': 2.0,
            'wind_cdir_full': 'западный'
        }
        
        save_json(test_data)
        
        self.assertTrue(os.path.exists("report.json"))
        
        with open("report.json", "r", encoding="utf-8") as f:
            content = json.load(f)
        
        self.assertEqual(content['city_name'], 'Тестовый город')
        self.assertEqual(content['temp'], 20)
        
        os.remove("report.json")

    def test_save_txt(self):
        """Простой тест для save_txt"""
        test_data = {
            'city_name': 'Тестовый город',
            'temp': 20,
            'app_temp': 22,
            'weather': {'description': 'облачно'},
            'rh': 50,
            'pres': 1000,
            'wind_spd': 2.0,
            'wind_cdir_full': 'западный'
        }
        
        save_txt(test_data)
        
        self.assertTrue(os.path.exists("report.txt"))
        
        with open("report.txt", "r", encoding="utf-8") as f:
            content = f.read()
        
        self.assertIn("Погода в Тестовый город", content)
        self.assertIn("Температура -- 20°C", content)
        self.assertIn("Облачность -- облачно", content)
        
        os.remove("report.txt")


if __name__ == '__main__':
    unittest.main()


