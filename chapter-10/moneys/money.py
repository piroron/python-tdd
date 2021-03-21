"""通貨基底クラス"""
from __future__ import annotations

class Money(object):
    """通貨の継承元"""

    def __init__(self, amount: int, currency: str) -> None:
        """初期化"""
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Money:
        """金額を指定倍して返す"""
        return Money(self._amount * multiplier, self.currency())

    def currency(self) -> str:
        """通貨単位"""
        return self._currency

    def __eq__(self, other: Money) -> bool:
        """override eq"""
        return (self._amount == other._amount) and (self.currency() == other.currency())

    @staticmethod
    def dollar(amount: int) -> Money:
        """ドルを作成して、返す"""
        from .dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Money:
        """フランを作成して、返す"""
        from .franc import Franc
        return Franc(amount)

    def __repr__(self):
        """クラス表現"""
        return str(self._amount) + " " + self._currency
