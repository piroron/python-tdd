"""通貨変換インターフェイス"""
from abc import ABCMeta, abstractmethod

class CurrencyExchanger(metaclass=ABCMeta):
    """通貨変換の機能を提供します。"""

    @abstractmethod
    def rate(self, fromcurr: str, tocurr: str) -> int:
        """通貨の換算率を取得します。"""
        pass
