from ia.pecas import P3S
from random import sample


class J7S:
    def __init__(self):
        self.pecas = P3S()

        # criando as listas de 7 pecas para cada jogador
        self.ppc = sample(self.pecas.pecas(), 7)
        self.hpc = sample(self.pecas.pecas(), 7)

    def pc(self, valor_jogada: int):
        """calcula na lista de pecas atribuida ao jogador-pc
        se existe alguma peca com valor correspondente
        ao ultimo valor da jogada.

        :return: a peca escolhida automaticamente para o jogador-pc;
        """
        for peca in self.ppc:
            if (peca[0] == valor_jogada) or (peca[1] == valor_jogada):
                return peca

    def hm(self, numero_peca: int):
        """
        :return: a peca escolhida pelo jogador-humano;
        """
        return self.hpc[numero_peca]
