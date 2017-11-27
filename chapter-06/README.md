## 第６章　テスト不足に気付いたら

### 継承
Pythonでも、Javaと同じような継承は可能。

```python
"""通貨基底クラス"""

class Money(object):
    """通貨の継承元"""
    pass
```

よく考えたら、独自クラスは`object`を継承すべきなので、そう記述する 

### 親クラスの参照
`Dollar`が`Money`を継承するようにする。

* Dollarクラス

```python
from .money import Money

class Dollar(Money):
```

同一階層であっても、`import`句が無いと見えないので注意

### amountを親で定義する
Javaのように、フィールドが無い。そこで、

```python
"""通貨基底クラス"""

class Money(object):
    """通貨の継承元"""
    def __init__(self, amount: int) -> None:
        """初期化"""
        self._amount = amount
```

親クラスで`__init__`を実装する。

結果として、子クラスにある`__init__`は不要となるため、削除する。

`Franc`も同様の手順で修正する。  
本章の目的は、`.equals`メソッドの移動であり、それは`__eq__`の移動と同義。  
結果として、子クラスからは`__init__`と`__eq__`が消えた。