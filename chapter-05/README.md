## 第５章　原則をあえて破るとき

### 解説
ここでの「あえて破るとき」というのは、

*本来コピペは悪だが、最終的に重複排除するから許せ*

ということ。

### Francをテストに追加
```
.E.
======================================================================
ERROR: test_franc_multiplication (tests.moneytests.MoneyTest)
フランの計算
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 20, in test_franc_multiplication
    five = Franc(5)
NameError: name 'Franc' is not defined

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (errors=1)
```

テストには失敗する。

### Francクラスの追加
```python
"""fran通貨"""

class Franc:
    """フラン通貨を表します。"""
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other: "Franc") -> bool:
        """override eq"""
        return self._amount == other._amount

    def times(self, multiplier: int) -> "Franc":
        """通貨変換"""
        return Franc(self._amount * multiplier)

```

単に、Dollarをコピーして、Francで置き換える

* テスト  

```python
from moneys.franc import Franc
```

の一文を追加することで、テストは成功するようになる