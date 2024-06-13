"""
if文を用いて、以下の条件分岐をするコードを記述してください。値はprint関数で出力してください。

・変数varが、3の倍数の場合は「Fizz」を出力
・変数varが、5の倍数の場合は「Buzz」を出力
・変数varが、3の倍数と5の倍数の両方に該当する場合は「FizzBuzz」を出力
・上記のどの場合にも該当しない場合は、変数varの値を出力

ただし、変数varは正の整数とします。
"""
#var = 15
"""
import random
var = random.randint(0,101)
print(var)
#print(type(var))
"""

#・変数varが、3の倍数と5の倍数の両方に該当する場合は「FizzBuzz」を出力
if var % 3 == 0 and var % 5 ==0:
#if var % 15 == 0:
  print("FizzBuzz")

#・変数varが、3の倍数の場合は「Fizz」を出力
elif var % 3 == 0:
  print("Fizz")

#・変数varが、5の倍数の場合は「Buzz」を出力
elif var % 5 == 0:
  print("Buzz")

#・上記のどの場合にも該当しない場合は、変数varの値を出力
else:
  print(var)