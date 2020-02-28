'''
@Date: 2020-02-28 14:47:24
@LastEditors: gxm
@LastEditTime: 2020-02-28 15:04:00
@FilePath: \Python workplace\code\day04\CRAPS赌博游戏.py
**说明**：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
'''
import random
money = 1000
while money > 0:
  print('总资产为：',money)
  go_on = False
  while True:
    debt = int(input('请下注:'))
    if 0 < debt <= money:
      break
  first = random.randint(1,6) + random.randint(1,6)
  print('f 玩家掷出%d点'% first)
  if first == 7 or first == 11:
    print('玩家胜')
    money += debt
  elif first == 2 or first == 3 or first == 12:
    print('庄家胜')
    money -= debt
  else:
    go_on = True
  while go_on:
    go_on = False
    num = random.randint(1,6) + random.randint(1,6)
    print('s 玩家掷出%d点'% num)
    if num == 7:
      print('庄家胜')
      money -= debt
    elif num == first:
      print('玩家胜')
      money += debt
    else:
      go_on = True
print('没钱了')