'''
@Date: 2020-02-28 14:36:54
@LastEditors: gxm
@LastEditTime: 2020-02-28 14:44:21
@FilePath: \Python workplace\code\day04\百钱百鸡.py
'''
for i in range(1,20):
  for j in range(1,33):
    z = 100 - i - j
    if 5 * i + 3 * j + z / 3 == 100:
      print('小鸡:%d,母鸡：%d,公鸡:%d'% (z,j,i))