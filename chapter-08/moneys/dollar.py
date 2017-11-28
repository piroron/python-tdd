"""dollar通貨"""
from .money import Money

class Dollar(Money):
    """ドル通貨を表します。"""
    def times(self, multiplier: int) -> Money:
        """通貨変換"""
        return Dollar(self._amount * multiplier)
