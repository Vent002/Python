'''
@Date: 2020-02-28 15:05:17
@LastEditors: gxm
@LastEditTime: 2020-02-28 15:08:03
@FilePath: \Python workplace\code\day04\斐波拉契数列.py
'''
f1 = 1
f2 = 1
for i in range(1,20):
  f = f1 + f2
  f1 = f2
  f2 = f
  print("第%d个 %d" % (i,f))