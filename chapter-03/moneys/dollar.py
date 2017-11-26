"""dollar通貨"""

class Dollar:
    """ドル通貨を表します。"""
    def __init__(self, amount: int) -> None:
        """初期化"""
        self.amount = amount

    def __eq__(self, other: "Dollar") -> bool:
        """override eq"""
        return self.amount == other.amount

    def times(self, multiplier: int) -> "Dollar":
        """通貨変換"""
        return Dollar(self.amount * multiplier)
