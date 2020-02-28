'''
@Date: 2020-02-28 15:08:43
@LastEditors: gxm
@LastEditTime: 2020-02-28 15:13:27
@FilePath: \Python workplace\code\day04\100以内素数.py
'''
import math
for i in range(2, 100):
  is_prime = True
  for j in range(2, int(math.sqrt(i)) + 1):
    if i % j == 0:
      is_prime = False
      break
  if is_prime:
    print('%d是素数'% i)