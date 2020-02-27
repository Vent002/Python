'''
@Date: 2020-02-27 18:50:38
@LastEditors: gxm
@LastEditTime: 2020-02-27 18:52:09
@FilePath: \Python workplace\code\day02\身份认证.py
'''
username = input('输入用户名：')
password = input('请输入密码：')
if username == 'admin' and password == 'admin':
  print('认证成功')
else:
  print('认证失败')