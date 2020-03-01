'''
@Date: 2020-03-01 10:04:31
@LastEditors: gxm
@LastEditTime: 2020-03-01 10:18:21
@FilePath: \Python workplace\code\day06\运算符.py
'''
print('hello' * 3) # hello hello hello
print('hello' * 3 + 'world') # hello hello hello world
print('ll' in 'hello') # True
print('world' in 'hello') # False
str = 'abcde12345'
# 索引下标从 0 开始
print(str[2]) # c
print(str[2:5]) # cde  单冒号表示从索引值到另一索引值
print(str[2:]) # cde12345 无开始索引或结尾索引 从头开始 到尾结束 
print(str[2::2]) # ce24 从索引2开始去偶数索引  双冒号
print(str[::2]) # ace24 偶数索引
print(str[:-1]) # abcde1234
print(str[-3:-1]) # 34