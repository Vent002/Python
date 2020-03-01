'''
@Date: 2020-03-01 11:57:00
@LastEditors: gxm
@LastEditTime: 2020-03-01 16:30:31
@FilePath: \Python workplace\code\day06\生成式和生成器.py
'''
import sys
f = [x for x in range(1,10)]
print(f,'\n')
f = [x + y for x in 'ABCDE' for y in '123456']
print(f,'\n')
f = [x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f),'\n')
print(f)

f = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(f))
for i in f :
  print(i)