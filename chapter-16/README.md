## 第１６章　将来の読み手を考えたテスト

### テスト追加
テスト自体は本と一緒

結果は以下の通り

```
..........E.
======================================================================
ERROR: test_total_times (tests.moneytests.MoneyTest)
moneyの倍
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 91, in test_total_times
    total = Total(five_bucks, ten_francs).times(2)
AttributeError: 'Total' object has no attribute 'times'

----------------------------------------------------------------------
Ran 12 tests in 0.003s

FAILED (errors=1)
```

`Total.times`が無い。

追加も本と一緒で良い。  
publicに引き上げる部分は不要

### Moneyを返す
一応書いた。

```python
def test_plus_samecurrency_money(self):
    """加算でMoneyを返す"""
    total = Money.dollar(1).plus(Money.dollar(1))
    self.assertIsInstance(total, Money)
```