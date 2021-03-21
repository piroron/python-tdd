"""dollar通貨"""
from __future__ import annotations

class Dollar:
    """ドル通貨を表します。"""
    def __init__(self, amount: int) -> None:
        """初期化"""
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        """通貨変換"""
        return Dollar(self.amount * multiplier)
