import random

from academia import Academia


class Usuario:
    def __init__(self, tipo, academia: Academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0


    def iniciar_treino(self):
        lista_pesos = self.academia.lista_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.lista_espacos_vazios()
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)

        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)

