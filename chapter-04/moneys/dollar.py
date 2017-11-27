"""dollar通貨"""

class Dollar:
    """ドル通貨を表します。"""
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other: "Dollar") -> bool:
        """override eq"""
        return self._amount == other._amount

    def times(self, multiplier: int) -> "Dollar":
        """通貨変換"""
        return Dollar(self._amount * multiplier)
