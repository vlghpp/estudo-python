from abc import ABC, abstractmethod


class Abstrata(ABC):

    @abstractmethod
    def implementar_metodo(self) -> None:
        pass

    @abstractmethod
    def outro_metodo(self) -> None:
        pass