class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0] # Chama-se compensação em lista
        self.porta_halteres = {}
        self.reiniciar_dia()


    def reiniciar_dia(self) -> None:
        self.porta_halteres = {i: i for i in self.halteres} # Chama-se compensação em dicionários

    def lista_espacos_vazios(self):
        return [i for i,j in self.porta_halteres.items() if j == 0]


    def lista_halteres(self) -> list :
        return [i for i in list(self.porta_halteres.values()) if i != 0]

    def pegar_haltere(self, halterRequerido: int) -> int:
        halter_pos = list(self.porta_halteres.values()).index(halterRequerido)
        key_halt = list(self.porta_halteres.keys()[halter_pos])
        self.porta_halteres[key_halt] = 0
        return halterRequerido

    def devolver_halter(self, pos, halt):
        self.porta_halteres[pos] = halt

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)