## 第８章　実装を隠す

### timesの戻り値型変更
Pythonでは、意味がない。  
このサンプル上、型アノテーションを使って書いているが、これはコンパイラには無視される。

### ファクトリメソッド
```
..E
======================================================================
ERROR: test_multiplication (tests.moneytests.MoneyTest)
金額を指定倍する
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 11, in test_multiplication
    five = Money.dollar(5)
AttributeError: type object 'Money' has no attribute 'dollar'

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (errors=1)
```

存在しない型を作るので、いったん失敗

### moneyにimportを追加

* money.py

```python
"""通貨基底クラス"""
from .dollar import Dollar

class Money(object):
    """通貨の継承元"""
    def __init__(self, amount: int) -> None:
        """初期化"""
        self._amount = amount

    def __eq__(self, other: "Money") -> bool:
        """override eq"""
        return (self._amount == other._amount) and \
            (self.__class__.__name__ == other.__class__.__name__)
    
    @staticmethod
    def dollar(amount: int) -> Dollar:
        """ドルを作成して、返す"""
        return Dollar(amount)

```

staticメソッドとして、`Dollar`の作成処理を追加する  
Pythonでstaticメソッドを利用する場合、`@staticmethod`と付ける

```
E
======================================================================
ERROR: moneytests (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: moneytests
Traceback (most recent call last):
  File "C:\Users\maste\AppData\Local\Programs\Python\Python36\lib\unittest\loader.py", line 153, in loadTestsFromName
    module = __import__(module_name)
  File "C:\dev\python\tdd\tests\moneytests.py", line 3, in <module>
    from moneys.dollar import Dollar
  File "C:\dev\python\tdd\moneys\dollar.py", line 2, in <module>
    from .money import Money
  File "C:\dev\python\tdd\moneys\money.py", line 2, in <module>
    from .dollar import Dollar
ImportError: cannot import name 'Dollar'


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

これではエラーになる。  
循環参照か？

[Qiitaの参考にしたリンク](https://qiita.com/puriketu99/items/a1347bf5200f095e486e)

上記に倣い、`dollar`メソッドを修正する。

```python
@staticmethod
def dollar(amount: int) -> "Dollar":
    """ドルを作成して、返す"""
    from .dollar import Dollar
    return Dollar(amount)
```

型アノテーションの`Dollar`は、モジュールのimportからDollarを消したため、参照できない。  
そのため、文字列に変更する

### Moneyにtimesを移動
本では、

> コンパイラが親切にMoney型にはtimesメソッドが定義されていないと教えてくれる。

とあるが、Pythonは教えてくれない。（ダックタイピング）

* moneytest.py

```python
def test_multiplication(self):
    """金額を指定倍する"""
    five: Money = Money.dollar(5)
    self.assertEqual(Dollar(10), five.times(2), "5 * 2")
    self.assertEqual(Dollar(15), five.times(3), "5 * 3")
```

という風に、`five`に型指定を入れても、Intellisense（予測変換）では出なくなるが、テストは通る。

Pythonは、仕組み上抽象メソッドは無いので、`ABCMeta`を使う