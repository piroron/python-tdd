## 第４章　意図を語るテスト

### 章に入る前に
テスト側のインポートで、クラスをインポートするように修正した。

* 修正前
```python
from moneys import dollar
```

* 修正後
```python
from moneys.dollar import Dollar
```

### インライン化
上記、インポート修正も含め、かなり見やすくなった

```python
def test_multiplication(self):
    """テスト"""
    five = Dollar(5)
    self.assertEqual(Dollar(10), five.times(2), "5 * 2")
    self.assertEqual(Dollar(15), five.times(3), "5 * 3")
```

### privateメンバーにする

Pythonは、Privateメンバーという概念が**無い**。  

[Pythonチュートリアル：プライベート変数](https://docs.python.jp/3/tutorial/classes.html#private-variables)

チュートリアルの記載に倣い、アンダースコアを付ける。

```python
class Dollar:
    """ドル通貨を表します。"""
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, other: "Dollar") -> bool:
        """override eq"""
        return self._amount == other._amount

    def times(self, multiplier: int) -> "Dollar":
        """通貨変換"""
        return Dollar(self._amount * multiplier)
```

`other._amount`の部分で、pylintが警告を出すが、問題があるソースではないため、無視して良いと考えられる。  
Javaならアクセス可能。

あえてamountを隠すなら、という実装。Pythonだとプロパティを利用したほうが良いように思う。  
