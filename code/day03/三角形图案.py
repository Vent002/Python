'''
@Date: 2020-02-27 20:58:22
@LastEditors: gxm
@LastEditTime: 2020-02-27 21:00:47
@FilePath: \Python workplace\code\day03\三角形图案.py
'''
import math
row = int(input('行数：'))
for i in range(0,row):
  for j in range(i+1):
    print('*',end='')
  print()