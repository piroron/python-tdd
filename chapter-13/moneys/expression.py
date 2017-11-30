"""式を表す"""
from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    """式（演算）を表します。"""

    @abstractmethod
    def reduce(self, currency: str) -> "Money":
        """式を単純な形に変形する"""
        pass
