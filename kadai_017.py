"""
名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。

Humanクラスには、以下の条件で標準出力(print)するcheck_adultメソッドを追加してください。

ageが20以上の場合に大人であること
そうでない場合に大人でないこと
Humanクラスのインスタンスを複数生成してリストに追加し、リストの要素数分だけcheck_adultメソッドを呼び出してください。
"""

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name} is adult.")
    else:
      print(f"{self.name} is not adult")

h1 = Human("Taro", 18)
h2 = Human("Samurai", 21)

human_list = []

human_list.append(h1)
human_list.append(h2)

for human in human_list:
  human.check_adult()