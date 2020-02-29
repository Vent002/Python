'''
@Date: 2020-02-29 11:01:07
@LastEditors: gxm
@LastEditTime: 2020-02-29 11:12:32
@FilePath: \Python workplace\code\day05\module\test.py
'''

'''
def foo():
  print('hello,python')

def foo():
  print('hello,world') # 后面的函数会覆盖之前的同名函数

foo() # hello,world
'''

import module1

module1.foo()

import module2
module2.foo()

import module3
# 导入module3时，不会执行模块中if条件成立时的代码 因为模块的名字是module3 不是 __main__

print(module3.foo())