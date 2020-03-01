'''
@Date: 2020-03-01 11:40:50
@LastEditors: gxm
@LastEditTime: 2020-03-01 11:44:44
@FilePath: \Python workplace\code\day06\列表添加元素移除元素.py
'''
list1 = [1,2,34,100]
list1.append(200)
list1.insert(1,300)
list1 += [1000,2000]
print(list1) # [1, 300, 2, 34, 100, 200, 1000, 2000]
print(len(list1)) # 8

if 2 in list1:
  list1.remove(2)
if 123 in list1:
  list1.remove(123)
print(list1) #[1, 300, 34, 100, 200, 1000, 2000]

list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)  # [300, 34, 100, 200, 1000]
list1.clear()
print(list1) #[]