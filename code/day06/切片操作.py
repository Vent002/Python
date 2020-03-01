'''
@Date: 2020-03-01 11:45:07
@LastEditors: gxm
@LastEditTime: 2020-03-01 11:48:43
@FilePath: \Python workplace\code\day06\切片操作.py
'''
fruits = ['grape','apple','strawberry','banana']
fruits += ['pitaya','pear','mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # ['apple', 'strawberry', 'banana']

fruits3 = fruits2[:]
print(fruits3) # ['apple', 'strawberry', 'banana']

fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'banana', 'strawberry', 'apple', 'grape']