"""
Weather App Package.

Модуль для получения и сохранения данных о погоде.

Модули:
    api - Функции для работы с Weatherbit API
    main - Основной исполняемый модуль
    save - Функции для сохранения данных

Примеры:
    >>> from weather_app import current_weather
    >>> data = current_weather("Москва")
    >>> from weather_app import save_json
    >>> save_json(data)
"""

from .api import current_weather
from .main import main
from .save import save_json,save_txt

__all__ = [
    "current_weather",
    "main",
    "save_json",
    "save_txt"
]