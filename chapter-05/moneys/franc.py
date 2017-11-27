"""fran通貨"""

class Franc:
    """フラン通貨を表します。"""
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other: "Franc") -> bool:
        """override eq"""
        return self._amount == other._amount

    def times(self, multiplier: int) -> "Franc":
        """通貨変換"""
        return Franc(self._amount * multiplier)
