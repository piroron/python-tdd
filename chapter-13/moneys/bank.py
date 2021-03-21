"""銀行"""
from .money import Expression, Money

class Bank(object):
    """銀行を表します。"""
    def reduce(self, source: Expression, currency: str) -> Money:
        """式を単純な形に変形する"""
        return source.reduce(currency)
