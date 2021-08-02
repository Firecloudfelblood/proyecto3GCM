import unittest
from Balanceados import parentesis_coherentes


class PruebaCoherentes(unittest.TestCase):

    def prueba(self, fun_solucion):
        dict_pruebas = {
            1: ('', True),
            2: ('{}', True),
            3: ('[]', True),
            4: ('(      )', True),
            5: ('asd()', True),
            6: ('asd()asd', True),
            7: ('asd{ asd }asd', True),
            8: ('a(a[aa{d}g245]g)2345$', True),
            10: ('{[[[[((())) ]]]] {} {} (())[][]}', True), -
            9: ('(]', False),
            10: ('asdasd(asd]}', False),
            11: ('[[[[]]])', False),
            12: ('{sd}{}{}[][]((ff', False),
            13: ('{', False),
            14: ('}{', False)
        }
        sol = 'Error, tu funcion no regresa nada'

        for p in dict_pruebas.values():
            try:
                sol = fun_solucion(cadena=p[0])
                self.assertEqual(sol, p[1])
            except AssertionError as e:
                print(f'Fallo! cadena={p[0]},  output={sol}, esperada={p[1]}')


t = PruebaCoherentes()
t.prueba(parentesis_coherentes)
