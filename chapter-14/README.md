## 第１４章　学習用テストと回帰テスト

### テスト

* moneytests.py

```python
def test_reducemoney_diff_currency(self):
    """別の貨幣へ変換"""
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    self.assertEqual(Money.dollar(1), result)
```

`pylint`が発行する警告に対応して、メソッド名（長すぎる）を修正

### Moneyの実装
* money.py
```python
def reduce(self, currency: str) -> "Money":
    rate = 2 if (self.currency() == "CHF" and currency == "USD") else 1
    return Money(self.amount() / rate, currency)
```

Python の三項演算子は、以下の通り。
```python
[trueで返す値] if ([条件式]) else [falseで返す値]
```

### bankの引数追加
`Sum`（ここでは`Total`）クラスの`reduce`に、`Bank`の引数を追加した。  
本では触れられていないが、これはインターフェイスの整合性のために追加されており、ここでは使う必要はない。

```python
def reduce(self, bank: Bank, currency: str) -> Money:
    """式を単純な形に変形する"""
    amount = self.augend().amount() + self.addend().amount()
    return Money(amount, currency)
```

問題となるのは、相互参照。  
循環参照が発生してしまう。

※ただし、引数の型指定を止めれば発生しないと思われる。

Bank ←→ Expression

が相互参照となるため、本とは異なるが、`Bank.rate`のインターフェイスを用意する。  
`CurrencyExchanger`インターフェイスを作成。

```python
"""通貨変換インターフェイス"""
from abc import ABCMeta, abstractmethod

class CurrencyExchanger(metaclass=ABCMeta):
    """通貨変換の機能を提供します。"""

    @abstractmethod
    def rate(self, fromcurr: str, tocurr: str) -> int:
        """通貨の換算率を取得します。"""
        pass
```

### Pairクラス
Pairクラスを、辞書のキーとして使おうとしている。

Pythonでは、辞書のキーとしてタプル（もしくは`frozenset`）を使ったほうが良い。
ここでは、タプルを使うこととする。  
→Pairクラスは登場しない

```python
class Bank(CurrencyExchanger):
    """銀行を表します。"""
    def __init__(self):
        self._rates = dict()

    def reduce(self, source: Expression, currency: str) -> Money:
        """式を単純な形に変形する"""
        return source.reduce(self, currency)

    def add_rate(self, fromcurr: str, tocurr: str, rate: int) -> None:
        """貨幣レートの変換登録"""
        self._rates[(fromcurr, tocurr)] = rate

    def rate(self, fromcurr: str, tocurr: str) -> int:
        """変換率を取得"""
        return self._rates.get((fromcurr, tocurr))
```


### 修正後テスト
```
....E...
======================================================================
ERROR: test_reduce_money (tests.moneytests.MoneyTest)
Moneyのテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 52, in test_reduce_money
    result = bank.reduce(Money.dollar(1), "USD")
  File "C:\dev\python\tdd\moneys\bank.py", line 13, in reduce
    return source.reduce(self, currency)
  File "C:\dev\python\tdd\moneys\money.py", line 32, in reduce
    return Money(self.amount() / rate, currency)
TypeError: unsupported operand type(s) for /: 'int' and 'NoneType'

----------------------------------------------------------------------
Ran 8 tests in 0.003s

FAILED (errors=1)
```

どうやら、`rate`の戻り値がおかしい模様（本と同じ）

回帰テストも、予想通り失敗する

```
FAIL: test_identity_rate (tests.moneytests.MoneyTest)
同一貨幣
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 64, in test_identity_rate
    self.assertEqual(1, Bank().rate("USD", "USD"))
AssertionError: 1 != None

----------------------------------------------------------------------
Ran 9 tests in 0.016s

FAILED (failures=1, errors=1)
```

`bank.py`の修正で直る。

```python
def rate(self, fromcurr: str, tocurr: str) -> int:
    """変換率を取得"""
    if fromcurr == tocurr:
        return 1
    return self._rates.get((fromcurr, tocurr))
```