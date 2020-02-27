'''
@Date: 2020-02-27 17:32:37
@LastEditors: gxm
@LastEditTime: 2020-02-27 17:43:00
@FilePath: \Python workplace\code\day01\平闰年.py
'''
year = int(input('输入年份：'))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print('闰年')
else:
  print('平年')