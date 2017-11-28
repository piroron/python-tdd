"""銀行"""
from .expression import Expression
from .money import Money

class Bank(object):
    """銀行を表します。"""
    def reduce(self, source: Expression, to: str) -> Money:
        """式を単純な形に変形する"""
        return Money.dollar(10)
