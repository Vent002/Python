'''
@Date: 2020-02-27 20:20:34
@LastEditors: gxm
@LastEditTime: 2020-02-27 20:22:03
@FilePath: \Python workplace\code\day03\for-in100以内偶数和.py
'''
sum = 0
for i in range(0,101,2):
  #if i % 2 == 0 :
    sum += i
print(sum)