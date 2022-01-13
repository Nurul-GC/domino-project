from ia.jogadores import J7S
from unittest import TestCase


class TestJogadores(TestCase):
    def test_humano(self):
        return self.assertTrue(
                J7S().hm()
        )

    def test_computador(self):
        return self.assertTrue(
                J7S().pc()
        )
