## 第２章　明白な実装

### Dollarの副作用

* 初回のエラー

```
======================================================================
ERROR: test_multiplication (tests.moneytests.MoneyTest)
テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 11, in test_multiplication
    self.assertEqual(10, product.amount, "5 * 2")
AttributeError: 'NoneType' object has no attribute 'amount'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

### 本との違い
Pythonでは、戻り値の型は推論して動くことから、**nullを返す**必要が無い。  

そもそも、型指定自体必要ないが、Python3.5以降の型アノテーションを利用し、戻り値型を指定している。

ただし、

```python
def times(self, multiplier: int) -> Dollar:
```

と定義を記載すると、`Dollarが見つからない`とエラーになる。  
（Dollarの定義が終わっていないため、らしい）

前方参照も無理そうなので、ここでは文字列で指定して、見て分かるようにしている。