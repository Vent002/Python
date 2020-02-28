'''
@Date: 2020-02-28 15:15:44
@LastEditors: gxm
@LastEditTime: 2020-02-28 15:20:26
@FilePath: \Python workplace\code\day04\完美数.py
**说明**：完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
'''
import math
for num in range(1,10000):
  result = 0
  for i in range(1,int(math.sqrt(num)) + 1): # math.sqrt(x) 返回 x 的平方根
    if num % i == 0:
      result += i
      if i > 1 and num // i != i:
        result += num // i
  if result == num:
    print(num)