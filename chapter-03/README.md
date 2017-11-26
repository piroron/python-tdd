## 第３章　三角測量

### 失敗例　その１

* ソース

```python
def test_equality(self):
    """同一性テスト"""
    self.assertTrue(dollar.Dollar(5) == dollar.Dollar(5))
```

* 結果

```
F.
======================================================================
FAIL: test_equality (tests.moneytests.MoneyTest)
同一性テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 17, in test_equality
    self.assertTrue(dollar.Dollar(5) == dollar.Dollar(5))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

失敗する。  
Pythonには、Javaの`equals`相当のメソッドが無いので、単に`==`で比較する。

### 失敗例　その２

Pythonで、Javaの`equals`と似た動きをさせるなら、`__eq__`を実装する

```python
def __eq__(self, other) -> bool:
    """override eq"""
    return True
```

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

成功はするが、テストを書き直すと

* テスト
```python
def test_equality(self):
    """同一性テスト"""
    self.assertTrue(dollar.Dollar(5) == dollar.Dollar(5), "$5 == $5")
    self.assertFalse(dollar.Dollar(5) == dollar.Dollar(6), "$5 != $6")
```

```
F.
======================================================================
FAIL: test_equality (tests.moneytests.MoneyTest)
同一性テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\dev\python\tdd\tests\moneytests.py", line 18, in test_equality
    self.assertFalse(dollar.Dollar(5) == dollar.Dollar(6), "$5 != $6")
AssertionError: True is not false : $5 != $6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

失敗する。

### 成功例

```python
def __eq__(self, other: "Dollar") -> bool:
    """override eq"""
    return self.amount == other.amount
```

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

引数に、文字列でDollarを指定すると、予測変換が可能になる。（Visual Studio Codeの場合）