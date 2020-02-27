'''
@Date: 2020-02-27 20:28:58
@LastEditors: gxm
@LastEditTime: 2020-02-27 20:31:42
@FilePath: \Python workplace\code\day03\九九乘法表.py
'''
for i in range(1,10): # 产生1~9的整数
  for j in range(1,i+1):
    print('%d * %d = %d' % (i,j,i*j),end='\t')
  print()