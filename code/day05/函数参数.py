'''
@Date: 2020-02-29 10:49:45
@LastEditors: gxm
@LastEditTime: 2020-02-29 10:59:56
@FilePath: \Python workplace\code\day05\函数参数.py
'''
import random
def roll_dice(n = 2): # 摇骰子
  total  = 0
  for i in range(0, n):
    total += random.randint(1,6)
  return total

def add(a = 0, b = 0, c = 0): # 三数相加
  return a + b + c

def addarg( *args ): # 参数名前加  *  表示该参数是可变参数
  total = 0
  for j in args:
    total += j
  return total

print(roll_dice())
print(add())
print(add(1,20))
print(add(c = 10, a = 1, b = 2))
print('addarg()无参',addarg())
print('addarg()一个参数',addarg(1))
print('addarg()两个参数',addarg(1,2))
print('addarg()三个参数',addarg(1,2,3))