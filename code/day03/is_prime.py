'''
@Date: 2020-02-27 20:32:22
@LastEditors: gxm
@LastEditTime: 2020-02-27 20:37:28
@FilePath: \Python workplace\code\day03\is_prime.py
'''
from math import sqrt
num = int(input('输入数：'))
is_prime = True
for i in (1,int(sqrt(num))+1):
  if num % i == 0:
    is_prime = False
    break
if(num != 1 and is_prime):
  print('%d是素数' % num)
else:
  print('%d不是素数' % num)