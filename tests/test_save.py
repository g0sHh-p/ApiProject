import unittest
import json
import os
from save import save_json, save_txt


class TestWeatherFunctionsSimple(unittest.TestCase):


    def test_save_json(self):
        
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
        
        os.remove("report.json")


    def test_save_txt(self):
       
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
        
        os.remove("report.txt")


if __name__ == '__main__':
    unittest.main()


