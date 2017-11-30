"""金額合計"""
from .money import Money
from .exchanger import CurrencyExchanger
from .expression import Expression

class Total(Expression):
    """金額の合計を表します。"""

    def __init__(self, augend: Money, addend: Money) -> None:
        """初期化"""
        self._augend = augend
        self._addend = addend

    def augend(self) -> Money:
        """被加算数"""
        return self._augend

    def addend(self) -> Money:
        """加算数"""
        return self._addend

    def reduce(self, bank: CurrencyExchanger, currency: str) -> Money:
        """式を単純な形に変形する"""
        amount = self.augend().amount() + self.addend().amount()
        return Money(amount, currency)
