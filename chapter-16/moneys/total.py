"""金額合計"""
from .money import Expression, Money
from .exchanger import CurrencyExchanger

class Total(Expression):
    """金額の合計を表します。"""

    def __init__(self, augend: Expression, addend: Expression) -> None:
        """初期化"""
        self._augend = augend
        self._addend = addend

    def augend(self) -> Expression:
        """被加算数"""
        return self._augend

    def addend(self) -> Expression:
        """加算数"""
        return self._addend

    def reduce(self, bank: CurrencyExchanger, currency: str) -> Money:
        """式を単純な形に変形する"""
        amount = self.augend().reduce(bank, currency).amount() + \
            self.addend().reduce(bank, currency).amount()
        return Money(amount, currency)

    def plus(self, addend: Expression) -> Expression:
        """加算"""
        return Total(self, addend)

    def times(self, multiplier: int) -> Expression:
        """指定倍"""
        return Total(self.augend().times(multiplier), self.addend().times(multiplier))
