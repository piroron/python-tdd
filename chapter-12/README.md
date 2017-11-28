## 第１２章　設計とメタファー

### 注意事項
本では、合計の変数名を`sum`としているが、Pythonだと、標準で同名のメソッドが存在する。  
安全性を考慮して、そこは変数名を変更している。

また、これまで`_amount`というフィールドにしていた値を、`amount()`メソッドで取得できるようにした。

```python
def amount(self) -> int:
    """金額"""
    return self._amount
```

### plusメソッドの追加
```python
def plus(self, addend: "Money") -> "Money":
    """加算"""
    return Money(self.amount() + addend.amount(), self.currency())
```

### Bank、Expressionの追加

インターフェイス`Expression`を追加する。  
が、Pythonにはinterfaceが無いので、抽象クラスで代用する。

※Pythonは多重継承をサポートしているので、抽象クラスで十分代用可能

* expression.py

```python
"""式を表す"""
from abc import ABCMeta

class Expression(metaclass=ABCMeta):
    """式（演算）を表します。"""
    pass
```

* bank.py

```python
"""銀行"""
from .expression import Expression
from .money import Money

class Bank(object):
    """銀行を表します。"""
    def reduce(self, source: Expression, to: str) -> Money:
        """式を単純な形に変形する"""
        return Money.dollar(10)
```