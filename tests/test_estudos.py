import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from chaves import sortear_chaves  # noqa: E402
from placar import aplicar  # noqa: E402
from preco import calcular_preco  # noqa: E402


class TestPlacar(unittest.TestCase):
    def test_pontuacao(self):
        self.assertEqual(aplicar("passagem", 2), (5, False))
        self.assertEqual(aplicar("MONTADA", 0), (4, False))

    def test_finalizacao_encerra(self):
        self.assertEqual(aplicar("finalização", 7), (7, True))

    def test_tecnica_invalida(self):
        with self.assertRaises(ValueError):
            aplicar("voadora", 0)


class TestChaves(unittest.TestCase):
    def test_par(self):
        pares = sortear_chaves(["A", "B", "C", "D"], semente=1)
        self.assertEqual(len(pares), 2)
        self.assertEqual({x for p in pares for x in p}, {"A", "B", "C", "D"})

    def test_impar_tem_bye(self):
        pares = sortear_chaves(["A", "B", "C"], semente=1)
        self.assertEqual(len(pares), 2)
        self.assertIsNone(pares[-1][1])

    def test_poucos_atletas(self):
        with self.assertRaises(ValueError):
            sortear_chaves(["A"])


class TestPreco(unittest.TestCase):
    def test_margem_30(self):
        r = calcular_preco(70, 30)
        self.assertAlmostEqual(r["preco_venda"], 100)
        self.assertAlmostEqual(r["lucro"], 30)

    def test_margem_invalida(self):
        with self.assertRaises(ValueError):
            calcular_preco(10, 100)

    def test_custo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_preco(-1, 10)


if __name__ == "__main__":
    unittest.main()
