#上辺：10cm
#下辺：20cm
#高さ：5cm

#公式：台形の面積 =（上辺＋下辺）× 高さ ÷ 2

#変数を定義
upper_base = 10
lower_base = 20
height = 5

area = (upper_base + lower_base) * height / 2

#出力
#\u00B2はUnicode文字
# Pythonの文字列で上付き文字（スーパースクリプト）を表現したい場合使用
print(f"{area} cm\u00B2")
