# python-tdd
『テスト駆動開発』に出てくるサンプルを、Pythonで実装したものです。

## versions

|種類|バージョン|
|---|---|
|Python|3.9.2|
|Visual Studio Code|1.54.3|
|Pylance|2021.3.2|

## ルール
このソースでは、Pythonの「型アノテーション」を用いるようにします。また、`Pylance`で警告が出ないようにしています。

## テストの実行
それぞれのchapterのディレクトリに移動し、以下のコマンドを実行します。

```python
python -m unittest tests/moneytests.py
```
