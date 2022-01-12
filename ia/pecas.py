from pprint import pprint


class P3S:
    def domino(self, numero_peca: int):
        """Um dominó refere-se
        a uma peça do jogo.

        :param numero_peca: numero referente a peca desejada de 0 a 27.
        :return: uma tupla com os valores da peca escolhida.
        """
        return self.pecas()[numero_peca]

    def valores(self, valor1: int):
        """define os valores de cada peca"""
        p = []
        for valor2 in range(valor1, 7):
            p.append((valor1, valor2))
        return p

    def pecas(self):
        """:return: retorna todas as pecas do jogo em uma lista."""
        p = []
        for v1 in range(7):
            for vls in self.valores(v1):
                p.append(vls)
        return p
