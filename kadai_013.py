"""
商品を購入して、消費税を加えた計算結果を返す関数を記述してください。
第1引数に商品の金額、第2引数に消費税（10%）を設定できるようにしてください。

計算結果で小数点が含まれる場合はそのまま表示してください。
切り捨てや四捨五入などの処理は不要です。

"""


def calculate_total(price:int, tax:int) ->int:
  total = price * ((100 + tax) / 100)

  return total

#calculate_total(1200, 10)