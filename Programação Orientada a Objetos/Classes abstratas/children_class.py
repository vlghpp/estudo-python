from abstract_class import Abstrata

class Filha(Abstrata):
    def __init__(self, nome):
        self.nome = nome


    @classmethod
    def ola_print(self) -> str:
        return f"Olá, {self.nome}"



    def outro_metodo(self) -> None:
        pass

    def implementar_metodo(self) -> None:
        pass