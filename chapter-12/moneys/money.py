"""通貨クラス"""
from .expression import Expression

class Money(Expression):
    """通貨"""

    def __init__(self, amount: int, currency: str) -> None:
        """初期化"""
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> "Money":
        """金額を指定倍して返す"""
        return Money(self.amount() * multiplier, self.currency())

    def amount(self) -> int:
        """金額"""
        return self._amount

    def currency(self) -> str:
        """通貨単位"""
        return self._currency

    def plus(self, addend: "Money") -> Expression:
        """加算"""
        return Money(self.amount() + addend.amount(), self.currency())

    @staticmethod
    def dollar(amount: int) -> "Money":
        """ドルを作成して、返す"""
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> "Money":
        """フランを作成して、返す"""
        return Money(amount, "CHF")

    def __eq__(self, other: "Money") -> bool:
        """override eq"""
        return (self.amount() == other.amount()) and (self.currency() == other.currency())

    def __repr__(self):
        """クラス表現"""
        return str(self.amount()) + " " + self.currency()
