'''
@Date: 2020-02-27 20:22:36
@LastEditors: gxm
@LastEditTime: 2020-02-27 20:27:56
@FilePath: \Python workplace\code\day03\while猜数游戏.py
'''
import random
answer = random.randint(1,100)
counter = 0
while True:
  counter += 1
  number = int(input('输入数：'))
  if number > answer:
    print('猜大了')
  elif number < answer:
    print('猜小了')
  else:
    print('猜对了')
    break
print('总共猜了%d次'% counter)
if counter > 8 :
  print('游戏结束')