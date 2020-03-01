'''
@Date: 2020-03-01 11:34:11
@LastEditors: gxm
@LastEditTime: 2020-03-01 11:38:04
@FilePath: \Python workplace\code\day06\列表的基本操作.py
'''
list1 = [1,2,3,4,5,100]
print(list1)
list2 = ['hello'] * 3
print(list2)
print(len(list2))
print(list1[0])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] = 300
print(list1)

for index in range(len(list1)):
  print(list1[index])

for elem in list1:
  print(elem)

for index,elem in enumerate(list1):
  print(index,elem)