import json


def save_json(data):
    
    with open("report.json","w",encoding="utf-8") as f:
        
        json.dump(data,f,ensure_ascii=False,indent=4)
        
    
    
def save_txt(data):
    
    text = f"""
    Погода в {data['city_name']}
    Температура -- {data['temp']}°C
    Ощущается как -- {data['app_temp']}°C
    Облачность -- {data['weather']['description']}
    Влажность -- {data['rh']}%
    Давление -- {data['pres']} hPa
    Скорость ветра -- {data['wind_spd']} м/с
    Направление ветра -- {data['wind_cdir_full']}"""
    
    with open("report.txt","w",encoding="utf-8") as f:
    
        f.write(text)                