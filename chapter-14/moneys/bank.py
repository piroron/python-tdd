"""銀行"""
from .money import Money
from .exchanger import CurrencyExchanger
from .expression import Expression

class Bank(CurrencyExchanger):
    """銀行を表します。"""
    def __init__(self):
        self._rates = dict()

    def reduce(self, source: Expression, currency: str) -> Money:
        """式を単純な形に変形する"""
        return source.reduce(self, currency)

    def add_rate(self, fromcurr: str, tocurr: str, rate: int) -> None:
        """貨幣レートの変換登録"""
        self._rates[(fromcurr, tocurr)] = rate

    def rate(self, fromcurr: str, tocurr: str) -> int:
        """変換率を取得"""
        if fromcurr == tocurr:
            return 1
        return self._rates.get((fromcurr, tocurr))
