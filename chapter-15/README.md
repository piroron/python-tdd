## 第１５章　テスト任せとコンパイラ任せ

### テストの追加

```python
def test_mixed_addition(self):
    """異なる通貨の加算"""
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(five_bucks.plus(ten_francs), "USD")
    self.assertEqual(Money.dollar(10), result)
```

本では、

> 大量のコンパイルエラーが出る

とあるが、一つも出ない。  
`five_bucks`が、型指定なしで`Money`と扱われているため。

テストは、以下の通り失敗する。

```
...F......
======================================================================
FAIL: test_mixed_addition (tests.moneytests.MoneyTest)
異なる通貨の加算
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 73, in test_mixed_addition
    self.assertEqual(Money.dollar(10), result)
AssertionError: 10 USD != 15 USD

----------------------------------------------------------------------
Ran 10 tests in 0.003s

FAILED (failures=1)
```

### テストを通す
```python
def reduce(self, bank: CurrencyExchanger, currency: str) -> Money:
    """式を単純な形に変形する"""
    amount = self.augend().reduce(bank, currency).amount() + \
        self.addend().reduce(bank, currency).amount()
    return Money(amount, currency)
```

１行が長すぎると、`pylint`の警告に該当するため、二行に分ける

### plusをExpressionに追加

* expression.py

```python
@abstractmethod
def plus(self, addend: "Expression") -> "Expression":
    """加算"""
    pass
```

自身は参照できないため、型は文字列。

いっぱいエラーが出る。
```
...E.E..EE
======================================================================
ERROR: test_mixed_addition (tests.moneytests.MoneyTest)
異なる通貨の加算
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 72, in test_mixed_addition
    result = bank.reduce(five_bucks.plus(ten_francs), "USD")
  File "C:\dev\python\tdd\moneys\money.py", line 28, in plus
    return Total(self, addend)
TypeError: Can't instantiate abstract class Total with abstract methods plus

======================================================================
ERROR: test_plus_returnsum (tests.moneytests.MoneyTest)
合計を返す場合のテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 37, in test_plus_returnsum
    result = five.plus(five)
  File "C:\dev\python\tdd\moneys\money.py", line 28, in plus
    return Total(self, addend)
TypeError: Can't instantiate abstract class Total with abstract methods plus

======================================================================
ERROR: test_reducesum (tests.moneytests.MoneyTest)
合計のテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 44, in test_reducesum
    total = Total(Money.dollar(3), Money.dollar(4))
TypeError: Can't instantiate abstract class Total with abstract methods plus

======================================================================
ERROR: test_simple_addition (tests.moneytests.MoneyTest)
同一単位の加算
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 29, in test_simple_addition
    total = five.plus(five)
  File "C:\dev\python\tdd\moneys\money.py", line 28, in plus
    return Total(self, addend)
TypeError: Can't instantiate abstract class Total with abstract methods plus

----------------------------------------------------------------------
Ran 10 tests in 0.004s

FAILED (errors=4)
```

MoneyはPlusを持っていないため、エラーになる