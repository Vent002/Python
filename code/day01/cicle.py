'''
@Date: 2020-02-27 17:29:07
@LastEditors: gxm
@LastEditTime: 2020-02-27 17:31:54
@FilePath: \Python workplace\code\day01\cicle.py
'''
import math
radius = float(input('输入半径:'))
perimeter = 2 * radius * math.pi
area = math.pi * radius * radius
print('周长：%.1f' % perimeter)
print('面积：%.1f' % area)