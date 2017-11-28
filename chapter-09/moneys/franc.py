"""fran通貨"""
from .money import Money

class Franc(Money):
    """フラン通貨を表します。"""

    def __init__(self, amount: int) -> None:
        """初期化"""
        Money.__init__(self, amount, "CHF")

    def times(self, multiplier: int) -> Money:
        """通貨変換"""
        return Money.franc(self._amount * multiplier)
