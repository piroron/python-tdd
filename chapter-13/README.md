## 第１３章　実装を導くテスト

前章から引き続き、`Sum`は`Total`として表現する。

### キャスト
Pythonは型指定が無いので、本で指定されるようなアップキャストは、あまり意味がない。

### Sumクラス（Totalクラス）
Pythonはインターフェイスが無いため、抽象クラスで代用するのは、１２章で述べた通り。  

```python
"""金額合計"""
from. expression import Expression
from .money import Money

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
```

### reduce関連

* total.py

```python
def reduce(self, currency: str) -> Money:
    """式を単純な形に変形する"""
    amount = self.augend().amount() + self.addend().amount()
    return Money(amount, currency)
```

* money.py

```python
def reduce(self, currency: str) -> "Money":
    return self
```

`Money`は、自身の`Money`を解決できないため、戻り値型を文字列にする

* bank.py

```python
def reduce(self, source: Expression, currency: str) -> Money:
    """式を単純な形に変形する"""
    return source.reduce(currency)
```

本には、

> キーワード引数を扱えるようなプログラミング言語であれば、差異を際立たせることが可能

と書いてあるが、よくわからないので、本と同じ実装になっている。