import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivisionExacta(self):
        valor_esperado = 'La división es exacta. \n' \
                         'Cociente: 9\n' \
                         'Residuo: 0'
        valor_actual = evaluar(45, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
class TestDivisionNoExacta(unittest.TestCase):
    def test_division_no_exacta(self):
        valor_esperado = 'La división no es exacta.\nCociente: 4\nResiduo: 1'
        valor_actual = evaluar(13, 3)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
