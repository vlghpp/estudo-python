from abc import ABC, abstractmethod


class ImpressaoInterface(ABC):
    @abstractmethod
    def imprimir_relatorio(self) -> None:
        pass