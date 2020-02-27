'''
@Date: 2020-02-27 19:01:39
@LastEditors: gxm
@LastEditTime: 2020-02-27 19:19:17
@FilePath: \Python workplace\code\day02\百分制等级判断.py
'''
score = float(input('输入成绩：'))
if score <= 100 and score >= 90:
  grade = 'A'
elif score < 90 and score >= 80:
  grade = 'B'
elif score < 80 and score >= 60:
  grade = 'C'
elif score >= 0 and score < 60:
  grade = 'D'
else:
  print('输入成绩无效')
print('对应等级：',grade)