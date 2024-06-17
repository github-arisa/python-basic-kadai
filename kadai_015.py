"""
名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。
nameとageを標準出力(print)するメソッド(printinfo)を追加してください。

Humanクラスのインスタンスは、変数に代入してプログラム内で使用してください。
"""

class Human():
  def __init__(self, name:str, age:int):
    self.name = name
    self.age = age

  def printinfo(self):
    print(self.name)
    print(self.age)

human = Human("Taro", 38)
human.printinfo()


