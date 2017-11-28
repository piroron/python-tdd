## 第９章　歩幅の調整

### currencyの追加
`Money`に、抽象メソッド`currency`を追加する。

```python
@abstractmethod
def currency(self) -> str:
    """通貨単位"""
    pass
```

第８章で見せられなかったが、`ABCMeta`を使うと、子クラスで`@abstractmethod`相当のメソッドを実装していないと、下記のようにエラーになる。

```
EEEE
======================================================================
ERROR: test_currency (tests.moneytests.MoneyTest)
通貨単位のテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 29, in test_currency
    self.assertEqual("USD", Money.dollar(1).currency(), "Dollar Unit")
  File "C:\dev\python\tdd\moneys\money.py", line 30, in dollar
    return Dollar(amount)
TypeError: Can't instantiate abstract class Dollar with abstract methods currency
```

本章は、本にあるJavaの例とやることはほとんど変わらない。

ただ、現状、本のコンストラクタ定義と、Pythonでのコンストラクタ定義が異なる。  
（６章から違っていたけど、スルーしていた）