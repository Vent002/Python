'''
@Date: 2020-02-28 14:28:07
@LastEditors: gxm
@LastEditTime: 2020-02-28 14:33:01
@FilePath: \Python workplace\code\day04\水仙花数.py
'''
for num in range(100,1000):
  x = num // 100 #百位
  y = num // 10 % 10 # 十位
  z = num % 10 # 个位
  if num == x ** 3 + y ** 3 + z ** 3: # ** 表示指数
    print(num)