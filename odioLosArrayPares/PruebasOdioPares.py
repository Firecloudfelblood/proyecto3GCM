import unittest
from OdioPares import respuesta_pares

class PruebaOdioPares(unittest.TestCase):

  def prueba(self, fun_solucion):
    dict_pruebas = {
        1:('101001','10'),
        2: ('1', '1'),
        3: ('0', '0'),
        4: ('', 'Helado es el vacio'),
        5: ('11', 'Helado es el vacio'),
        6: ('0011', 'Helado es el vacio'),
        7: ('1001', 'Helado es el vacio'),
        8: ('101', '101'),
        10: ('1001', 'Helado es el vacio'),
        9: ('10001', '101'),
        10: ('100001', 'Helado es el vacio'),
        11: ('1000001', '101'),
    }
    sol = 'Error, tu funcion no regresa nada'

    for p in dict_pruebas.values():
      try:
        sol = fun_solucion(arr=p[0])
        self.assertEqual(sol, p[1])
      except AssertionError as e:
        print(f'Fallo! cadena={p[0]},  output={sol}, esperada={p[1]}')
25
t = PruebaOdioPares()
t.prueba(respuesta_pares)