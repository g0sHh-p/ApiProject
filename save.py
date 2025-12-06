import json


def save_json(data):
    """
    Сохранить данные о погоде в формате JSON.

    Эта функция принимает словарь с данными о погоде и сохраняет его
    в файл report.json с форматированием и поддержкой кириллицы.

    :param data: Словарь с данными о погоде
    :type data: dict
    :return: None
    """
    
    with open("report.json","w",encoding="utf-8") as f:
    
        json.dump(data,f,ensure_ascii=False,indent=4)
    
    
def save_txt(data):
    """
    Сохранить данные о погоде в текстовом формате.

    Эта функция форматирует данные о погоде в читаемый текст
    и сохраняет в файл report.txt.

    :param data: Словарь с данными о погоде
    :type data: dict
    :return: None
    """
    
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