"""通貨クラス"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from .exchanger import CurrencyExchanger

class Expression(metaclass=ABCMeta):
    """式（演算）を表します。"""

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:
        """加算"""
        pass

    @abstractmethod
    def reduce(self, bank: CurrencyExchanger, currency: str) -> Money:
        """式を単純な形に変形する"""
        pass


class Money(Expression):
    """通貨"""

    def __init__(self, amount: int, currency: str) -> None:
        """初期化"""
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Expression:
        """金額を指定倍して返す"""
        return Money(self.amount() * multiplier, self.currency())

    def amount(self) -> int:
        """金額"""
        return self._amount

    def currency(self) -> str:
        """通貨単位"""
        return self._currency

    def plus(self, addend: Expression) -> Expression:
        """加算"""
        from .total import Total
        return Total(self, addend)

    def reduce(self, bank: CurrencyExchanger, currency: str) -> Money:
        rate = bank.rate(self.currency(), currency)
        return Money(self.amount() // rate, currency)

    @staticmethod
    def dollar(amount: int) -> Money:
        """ドルを作成して、返す"""
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        """フランを作成して、返す"""
        return Money(amount, "CHF")

    def __eq__(self, other: Money) -> bool:
        """override eq"""
        return (self.amount() == other.amount()) and (self.currency() == other.currency())

    def __repr__(self):
        """クラス表現"""
        return str(self.amount()) + " " + self.currency()
