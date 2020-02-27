'''
@Date: 2020-02-27 19:07:06
@LastEditors: gxm
@LastEditTime: 2020-02-27 19:13:24
@FilePath: \Python workplace\code\day02\三角形周长面积.py
'''
x = float(input('输入三角形边长X：'))
y = float(input('输入三角形边长Y：'))
z = float(input('输入三角形边长Z：'))
if x + y > z or x + z > y or y + z > x:
  print('周长%.1f',x+y+z)
  p = (x+y+z)/2
  area = (p*(p-x)*(p-y)*(p-z)**0.5) # ** 表示 指数
  print('面积%.1f',area)
else:
  print('不能构成三角形')