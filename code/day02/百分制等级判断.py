'''
@Date: 2020-02-27 19:01:39
@LastEditors: gxm
@LastEditTime: 2020-02-27 19:05:43
@FilePath: \Python workplace\code\day02\百分制等级判断.py
'''
score = float(input('输入成绩：'))
if score <= 100 and score >= 90:
  print('A')
elif score < 90 and score >= 80:
  print('B')
elif score < 80 and score >= 60:
  print('C')
elif score >= 0 and score < 60:
  print('D')
else:
  print('输入成绩无效')