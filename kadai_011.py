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

print("forを利用して記述")
for i in range(2):
  for day in array:
    print(day)
    if i ==2:
      break

print("\n")

print("whileを利用して記述")
i = 1
while i <= 2:
  for day in array:
    print(day)
  i = i + 1