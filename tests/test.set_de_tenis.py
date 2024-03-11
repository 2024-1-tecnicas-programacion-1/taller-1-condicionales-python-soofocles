import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.set_de_tenis import evaluar

class TestSetDeTenis(unittest.TestCase):
    def test_aun_no_termina(self):
        valor_esperado = 'Aún no termina'
        valor_actual = evaluar(4, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_ganador_A(self):
        resultado_esperado = 'El ganador es el jugador A'
        resultado_actual = evaluar(7, 5)
        self.assertEqual(resultado_esperado, resultado_actual)

    def test_ganador_B(self):
        resultado_esperado = 'El ganador es el jugador B'
        resultado_actual = evaluar(3, 7)
        self.assertEqual(resultado_esperado, resultado_actual)

    def test_invalido(self):
        resultado_esperado = 'Inválido'
        resultado_actual = evaluar(8, 3)
        self.assertEqual(resultado_esperado, resultado_actual)
    

if __name__ == '__main__':
    unittest.main()
