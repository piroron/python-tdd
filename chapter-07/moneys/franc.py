"""fran通貨"""
from .money import Money

class Franc(Money):
    """フラン通貨を表します。"""
    def times(self, multiplier: int) -> "Franc":
        """通貨変換"""
        return Franc(self._amount * multiplier)
