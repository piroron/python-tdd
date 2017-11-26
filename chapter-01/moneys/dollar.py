"""dollar通貨"""

class Dollar:
    """ドル通貨を表します。"""
    def __init__(self, amount: int):
        """初期化"""
        self.amount = amount

    def times(self, multiplier: int):
        """通貨変換"""
        self.amount *= multiplier
