"""
リストの中身を先頭から全て取り出して、出力結果が以下のようになるプログラムを、for、while、それぞれを利用して記述して下さい。

array = ["水","金","地","火","木","土","天","海","冥"]

水
金
地
火
木
土
天
海
冥
水
金
地
火
木
土
天
海
冥
"""
array = ["水","金","地","火","木","土","天","海","冥"]

for date in array:
  print(date)

i = 1
while i < 2:
  for date in array:
    print(date)
  i += 1
