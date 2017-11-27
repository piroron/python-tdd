"""通貨基底クラス"""

class Money(object):
    """通貨の継承元"""
    def __init__(self, amount: int) -> None:
        """初期化"""
        self._amount = amount

    def __eq__(self, other: "Money") -> bool:
        """override eq"""
        return (self._amount == other._amount) and \
            (self.__class__.__name__ == other.__class__.__name__)
