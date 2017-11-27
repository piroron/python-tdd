## 第７章　疑念をテストに翻訳する

### ドルとフランの同一性
```
F..
======================================================================
FAIL: test_equality (tests.moneytests.MoneyTest)
同一性テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 20, in test_equality
    self.assertFalse(Franc(5) == Dollar(5), "f5 != $5")
AssertionError: True is not false : f5 != $5

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
```

同一ではない、というチェックをしたが、同一と判定。  
`Money`クラスでそう実装しているから。

### クラス名の取得
```python
classname = self.__class__.__name__
```
で取得できる。  
`self`の部分は、オブジェクトであればよい