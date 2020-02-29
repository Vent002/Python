'''
@Date: 2020-02-29 10:45:42
@LastEditors: gxm
@LastEditTime: 2020-02-29 10:49:23
@FilePath: \Python workplace\code\day05\定义函数.py
@ 函数定义求阶乘
'''
def factorial(num):
  result = 1
  for i in range(1,num + 1):
    result *= i
  return result


m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) + factorial(n))