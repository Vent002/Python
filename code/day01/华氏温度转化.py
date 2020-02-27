'''
@Date: 2020-02-27 17:26:43
@LastEditors: gxm
@LastEditTime: 2020-02-27 17:28:35
@FilePath: \Python workplace\code\day01\华氏温度转化.py
'''
a = float(input('请输入温度：'))
c = (a - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (a,c))