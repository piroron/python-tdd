"""dollar通貨"""
from .money import Money

class Dollar(Money):
    """ドル通貨を表します。"""

    def __init__(self, amount: int) -> None:
        """初期化"""
        Money.__init__(self, amount, "USD")
