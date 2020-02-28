'''
@Date: 2020-02-28 14:33:35
@LastEditors: gxm
@LastEditTime: 2020-02-28 14:38:47
@FilePath: \Python workplace\code\day04\正整数的反转.py
'''
num = int(input('输入数:'))
reversed_num = 0
while num > 0:
  reversed_num = reversed_num * 10 + num % 10
  num // 10
print(reversed_num)