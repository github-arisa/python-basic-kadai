"""
以下のコードを実行するとスコープに関するエラーが発生します。エラーを修正して、正しく計算結果が出力されるようにしてください。

price1 = 100
price2 = 200

def total():
    tax = 1.1
    return price1 + price2

print (total() * tax)

---> 回答として、以下の２通りのコードを記述する
"""


tax = 1.1

def total():
  price1 = 100
  price2 = 200
  return price1 + price2

print (total() * tax)

"""
グローバル変数はローカルでも使用可能なので、
以下でもOK
"""

price1 = 100
price2 = 200
tax = 1.1

def total():
  return price1 + price2

print (total() * tax)

