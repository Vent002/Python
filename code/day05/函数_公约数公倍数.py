'''
@Date: 2020-02-29 11:13:43
@LastEditors: gxm
@LastEditTime: 2020-02-29 11:18:07
@FilePath: \Python workplace\code\day05\函数_公约数公倍数.py
'''
# 用函数计算最大公约数和最小公倍数
def g(x,y): # 最大公约数
  (x,y) = (y,x) if x > y else (x,y)
  for i in range(x,0,-1):
    if x % i == 0 and y % i == 0:
      return i

def l(x,y): #最小公倍数
  return x * y // g(x,y)


x = int(input('x = '))
y = int(input('y = '))
print('最大公约数：',g(x,y))
print('最小公倍数: ',l(x,y))