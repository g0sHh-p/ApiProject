import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import main


class TestMain(unittest.TestCase):
    
    def test_main_without_cmd_flag(self):
        """Тест main без флага --cmd"""
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        
        if os.path.exists("report.json"):
            os.remove("report.json")
        
        
        original_argv = sys.argv.copy()
        
        try:
            sys.argv = ['main.py', 'Москва']
            
            main()
            
            self.assertTrue(os.path.exists("report.json"))
            
            if os.path.exists("report.json"):
                os.remove("report.json")
                
        finally:
            
            sys.argv = original_argv
            
            if os.path.exists("report.json"):
                os.remove("report.json")
    
    def test_main_with_cmd_flag(self):
        
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        original_argv = sys.argv.copy()
        
        try:
            sys.argv = ['main.py', 'Москва', '--cmd']
            
            main()
            
            self.assertFalse(os.path.exists("report.json"))
                
        finally:

            sys.argv = original_argv
    
    def test_main_with_invalid_city(self):
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")
        
        if os.path.exists("report.json"):
            os.remove("report.json")
        
        
        original_argv = sys.argv.copy()
        
        try:
            sys.argv = ['main.py', 'НесуществующийГород12345']
            
            
            try:
                main()
                
                self.assertFalse(os.path.exists("report.json"))
            except Exception as e:
                self.fail(f"main() не обработал ошибку: {e}")
                
        finally:
            
            sys.argv = original_argv
            
            if os.path.exists("report.json"):
                os.remove("report.json")
    
    def test_main_without_api_key(self):
        
        if not os.getenv("API_KEY"):
            
            original_argv = sys.argv.copy()
            try:
                sys.argv = ['main.py', 'Москва']
                try:
                    main()
                    
                    self.assertTrue(True)
                except Exception as e:
                    self.fail(f"main() не обработал отсутствие API ключа: {e}")
            finally:
                sys.argv = original_argv
        else:
            self.skipTest("API_KEY установлен, тест пропущен")


if __name__ == '__main__':
    unittest.main()

