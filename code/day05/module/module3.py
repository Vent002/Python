'''
@Date: 2020-02-29 11:08:30
@LastEditors: gxm
@LastEditTime: 2020-02-29 11:11:01
@FilePath: \Python workplace\code\day05\module\module3.py
'''
def foo():
  pass
def bar():
  pass

# __name__ 是python中一个隐含的变量，代表该模块的名字
# 只有被Python解释器直接执行的模块名字才是   __main__

if __name__ == '__main__':
  print('call foo()')
  foo()
  print('call bar()')
  bar()