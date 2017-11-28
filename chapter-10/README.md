## 第１０章　テストに聞いてみる

### timesメソッドでMoneyを返す
* franc.py

```python
def times(self, multiplier: int) -> Money:
    """通貨変換"""
    return Money(self._amount * multiplier, self.currency)
```

エラーになる。`ABCMeta`を適用したことで、抽象クラス扱いであるため。

```
..E.
======================================================================
ERROR: test_franc_multiplication (tests.moneytests.MoneyTest)
フランの計算
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 24, in test_franc_multiplication
    self.assertEqual(Money.franc(10), five.times(2), "f10 == f10")
  File "C:\dev\python\tdd\moneys\franc.py", line 13, in times
    return Money(self._amount * multiplier)
TypeError: Can't instantiate abstract class Money with abstract methods times

----------------------------------------------------------------------
Ran 4 tests in 0.008s

FAILED (errors=1)
```

### Moneyの抽象クラスを止める

継承として指定されていた、`metaclass=ABCMeta`を外し、`object`にする

```python
class Money(object):
    """通貨の継承元"""
```

テストはやはりエラーになる。

```
..F.
======================================================================
FAIL: test_franc_multiplication (tests.moneytests.MoneyTest)
フランの計算
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 24, in test_franc_multiplication
    self.assertEqual(Money.franc(10), five.times(2), "f10 == f10")
AssertionError: <moneys.franc.Franc object at 0x000002051E597080> != <moneys.money.Money object at 0x000002051E597048> : f10 == f10

----------------------------------------------------------------------
Ran 4 tests in 0.007s

FAILED (failures=1)
```

### toStringの実装
Javaの`toString`と同様の機能として、Pythoには`__repr__`がある。  
`Money`クラスで実装する。

```python
def __repr__(self):
    """クラス表現"""
    return str(self._amount) + " " + self._currency
```

エラーには変わりないが、メッセージが変わる

```
..F.
======================================================================
FAIL: test_franc_multiplication (tests.moneytests.MoneyTest)
フランの計算
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 24, in test_franc_multiplication
    self.assertEqual(Money.franc(10), five.times(2), "f10 == f10")
AssertionError: 10 CHF != <moneys.money.Money object at 0x000001F3C5A470B8> : f10 == f10

----------------------------------------------------------------------
Ran 4 tests in 0.006s

FAILED (failures=1)
```

ただ、Javaと違って、親クラスの`toString`が引き継がれるわけでは無い模様

### FrancとMoneyの比較
テストを追加する。

```python
def test_differentclass_equality(self):
    """異なる通貨の同一性テスト"""
    self.assertTrue(Money(10, "CHF") == Franc(10), "Money = Franc")
```

失敗する。

```
.F...
======================================================================
FAIL: test_differentclass_equality (tests.moneytests.MoneyTest)
異なる通貨の同一性テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 35, in test_differentclass_equality
    self.assertTrue(Money(10, "CHF") == Franc(10), "Money = Franc")
AssertionError: False is not true : Money = Franc

----------------------------------------------------------------------
Ran 5 tests in 0.003s

FAILED (failures=1)
```

### `__eq__`の修正

```python
def __eq__(self, other: "Money") -> bool:
    """override eq"""
    return (self._amount == other._amount) and (self.currency() == other.currency())
```

`currency`を見るよう、修正する


### timesの移動
本に従って、`times`を`Money`に移動させる。

その結果、`Money`クラスは

```python
"""通貨基底クラス"""

class Money(object):
    """通貨の継承元"""
```

のように、`ABCMeta`と`abstractmethod`のインポートが不要となった。（抽象クラスではなくなった）