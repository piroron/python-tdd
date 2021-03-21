"""dollar通貨"""
from __future__ import annotations
from .money import Money

class Dollar(Money):
    """ドル通貨を表します。"""
    def times(self, multiplier: int) -> Dollar:
        """通貨変換"""
        return Dollar(self._amount * multiplier)
