from ia.pecas import P3S
from random import sample


class J7S:
    def __init__(self):
        self.pecas = P3S()

        # criando as listas de 7 pecas para cada jogador
        self.pecas_pc = sample(self.pecas.pecas(), 7)
        self.pecas_hm = sample(self.pecas.pecas(), 7)

        # definindo em variavel a quantidade de pecas que cada jogador tem
        self.qppc = len(self.pecas_pc)
        self.qhpc = len(self.pecas_hm)

    def pc(self, valor_jogada: int):
        """calcula na lista de pecas atribuida ao jogador-pc
        se existe alguma peca com valor correspondente
        ao ultimo valor da jogada.

        :return: a peca escolhida automaticamente para o jogador-pc;
        """
        for peca in self.pecas_pc:
            if (peca[0] == valor_jogada) or (peca[1] == valor_jogada):
                self.qppc -= 1
                return peca

    def hm(self, numero_peca: int):
        """
        :return: a peca escolhida pelo jogador-humano;
        """
        self.qhpc -= 1
        return self.pecas_hm[numero_peca]
