'''
@Date: 2020-03-01 10:25:04
@LastEditors: gxm
@LastEditTime: 2020-03-01 10:39:50
@FilePath: \Python workplace\code\day06\处理字符方法.py
'''
str1 = 'hello,world'
print(str1.upper()) # HELLO,WORLD
print(len(str1)) # 11
print(str1.capitalize()) # Hello,world
print(str1.title()) # Hello,World
print(str1.find('o')) # 4
print(str1.find('python')) # -1
print(str1.startswith('he')) # True
print(str1.endswith('LD')) # False
print(str1.center(50,'*')) # *******************hello,world********************
print(str1.rjust(50,' ')) #                                        hello,world
str2 = 'abc123456'
print(str2.isalnum()) # True
print(str2.isdigit()) # False
print(str2.isalpha()) # False
str3 = '  gxm@123.com  '
print(str3) #   gxm@123.com
print(str3.strip()) # gxm@123.com