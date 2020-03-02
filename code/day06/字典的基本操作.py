'''
@Date: 2020-03-02 20:04:39
@LastEditors: gxm
@LastEditTime: 2020-03-02 20:58:05
@FilePath: \Python workplace\code\day06\字典的基本操作.py
'''
# 创建字典的字面量语法
person = {'name':'tom','sex':'男','age':10} 

print(person) # {'name': 'tom', 'sex': '男', 'age': 10}

# 创建字典的构造器语法
items1 = dict(one=1,two = 2, three = 4,four = 4)

# 创建zip函数将两个序列压成字典

items2 = dict(zip(['a','b','b'],'123'))

# 创建字典的推导是语法

items3 = {num:num ** 3 for num in range(1,3)}
print(items1,items2,items3) # {'one': 1, 'two': 2, 'three': 4, 'four': 4}
                            # {'a': '1', 'b': '3'} 
                            # {1: 1, 2: 8}

# 通过键获取对应的值
print(person['name']) 

# 对字典中所有键值对进行遍历
for key in person:
  print(f'{key}:{person[key]}')
  
# get 通过键值获取对应的值 并设置默认值
print(person.get('name','nancy'))

# 删除字典中的元素
print(person.popitem())
print(person.pop('sex','男'))

# 清空字典
person.clear()
print(person)