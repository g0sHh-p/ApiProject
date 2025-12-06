import unittest
import sys
import os
from weather.main import main


class TestMain(unittest.TestCase):
    
    def test_main_without_cmd_flag(self):
        """Тест main без флага --cmd"""
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        # Удаляем файл если существует
        if os.path.exists("report.json"):
            os.remove("report.json")
        
        # Сохраняем оригинальные аргументы
        original_argv = sys.argv.copy()
        
        try:
            sys.argv = ['main.py', 'Москва']
            
            # Запускаем main
            main()
            
            # Проверяем, что файл был создан
            self.assertTrue(os.path.exists("report.json"))
            
            # Удаляем созданный файл
            if os.path.exists("report.json"):
                os.remove("report.json")
                
        finally:
            # Восстанавливаем оригинальные аргументы
            sys.argv = original_argv
            # Очищаем файл если остался
            if os.path.exists("report.json"):
                os.remove("report.json")
    
    def test_main_with_cmd_flag(self):
        """Тест main с флагом --cmd"""
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        # Сохраняем оригинальные аргументы
        original_argv = sys.argv.copy()
        
        try:
            sys.argv = ['main.py', 'Москва', '--cmd']
            
            # Запускаем main
            main()
            
            # При --cmd файл не должен создаваться
            self.assertFalse(os.path.exists("report.json"))
                
        finally:
            # Восстанавливаем оригинальные аргументы
            sys.argv = original_argv
    
    def test_main_with_invalid_city(self):
        """Тест main с несуществующим городом"""
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        # Удаляем файл если существует
        if os.path.exists("report.json"):
            os.remove("report.json")
        
        # Сохраняем оригинальные аргументы
        original_argv = sys.argv.copy()
        
        try:
            sys.argv = ['main.py', 'НесуществующийГород12345']
            
            # Функция должна обработать ошибку без падения
            try:
                main()
                # Файл не должен создаваться при ошибке
                self.assertFalse(os.path.exists("report.json"))
            except Exception as e:
                self.fail(f"main() не обработал ошибку: {e}")
                
        finally:
            # Восстанавливаем оригинальные аргументы
            sys.argv = original_argv
            # Очищаем файл если остался
            if os.path.exists("report.json"):
                os.remove("report.json")
    
    def test_main_without_api_key(self):
        """Тест main без API ключа"""
        # Этот тест сложно выполнить без моков, так как api_key загружается при импорте
        # Проверяем, что функция обрабатывает None от current_weather
        if not os.getenv("API_KEY"):
            # Если ключа нет, просто проверяем что функция не падает
            original_argv = sys.argv.copy()
            try:
                sys.argv = ['main.py', 'Москва']
                try:
                    main()
                    # Функция должна обработать отсутствие ключа без падения
                    self.assertTrue(True)
                except Exception as e:
                    self.fail(f"main() не обработал отсутствие API ключа: {e}")
            finally:
                sys.argv = original_argv
        else:
            self.skipTest("API_KEY установлен, тест пропущен")


if __name__ == '__main__':
    unittest.main()

