from unittest import TestCase
from ia.jogadores import J7S


class TestJogadores(TestCase):
    def test_humano(self):
        """testando o retorno da peca correspondente a jogada humana"""
        return self.assertTrue(
                J7S()  # chamando a classe do nosso script responsavel pela organizacao dos jogadores
                    .hm(5)  # chamando a funcao que retornara no terminal a peca corresdente a jogada
        )

    def test_computador(self):
        """testando o retorno da peca correspondente a jogada computador"""
        return self.assertTrue(
                J7S()  # chamando a classe do nosso script responsavel pela organizacao dos jogadores
                    .pc(5)  # chamando a funcao que retornara no terminal a peca corresdente a jogada
        )
