from unittest import TestCase
from ia.pecas import P3S


class TestPecas(TestCase):
    def test_domino(self):
        """testando a solicitacao de uma peca"""
        return self.assertTrue(
                P3S()  # chamando a classe do nosso script responsavel pela organizacao das pecas
                    .domino(numero_peca=5)  # chamando a funcao que imprimira no terminal a peca solicitada
        )

    def test_pecas(self):
        """testando a impressao de todas as pecas do jogo"""
        return self.assertTrue(
                P3S()  # chamando a classe do nosso script responsavel pela organizacao das pecas
                    .pecas()  # chamando a funcao que imprimira no terminal todas as pecas do jogo
        )
