import argparse
import json
from api import current_weather
from save import save_json,save_txt


def main():
    
    try:
        
        parser = argparse.ArgumentParser(description='city')

        parser.add_argument("city",type=str)
        parser.add_argument("--cmd",action="store_true",default=False)

        args = parser.parse_args()

        result = current_weather(city=args.city).json()
        
        data = result['data'][0]
        
        if args.cmd:
            
            print(f"============ Погода в {data['city_name']} ============")
            print()
            print(f"Температура -- {data['temp']}°C")
            print(f"Ощущается как -- {data['app_temp']}°C")
            print(f"Облачность -- {data['weather']['description']}")
            print(f"Влажность -- {data['rh']}%")
            print(f"Давление -- {data['pres']} hPa")
            print(f"Скорость ветра -- {data['wind_spd']} м/с")
            print(f"Направление ветра -- {data['wind_cdir_full']}")
            
        else:
            try:
                save_json(data)
            except:
                print("Ошибка сохранения данных")
        
    except KeyboardInterrupt:
        print("\nПрервано пользователем")
    except Exception as e:
        print(f"Ошибка: {e}")
    
if __name__ == "__main__":
    main()