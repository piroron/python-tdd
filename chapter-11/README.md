## 第１１章　不要になったら消す

### ファクトリの変更

* money.py

```python
@staticmethod
def dollar(amount: int) -> "Money":
    """ドルを作成して、返す"""
    from .dollar import Dollar
    return Money(amount, "USD")

@staticmethod
def franc(amount: int) -> "Money":
    """フランを作成して、返す"""
    from .franc import Franc
    return Money(amount, "CHF")
```

このようにすると、`pylint`が「不要なimportがある」と言ってくるので、消す。

全て本の通りに消す。