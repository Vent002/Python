'''
@Date: 2020-03-02 19:16:25
@LastEditors: gxm
@LastEditTime: 2020-03-02 19:34:35
@FilePath: \Python workplace\code\day06\元组基本操作.py
'''
# 定义元组
t = ('hsm',18,True,'beautiful') 
print(t) #('hsm', 18, True, 'beautiful')
# 获取元组中的元素
print(t[0])  #hsm
print(t[3])   #beautiful
#遍历元组中的值
for member in t :
  print(member) #hsm
                #18
                #True
                #beautiful
# 重新给元组赋值
t = ('gxm',20,True,'sichuan')
print(t) #('gxm', 20, True, 'sichuan')
#讲元组转换成列表
person = list(t)
print(person) #['gxm', 20, True, 'sichuan']
# 列表修改元素
person[0] = 'bruce'
person[1] = '21'
print(person) #['bruce', '21', True, 'sichuan']

# 讲列表转换成元组
fruits_list = ['apple','pear','orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)  #('apple', 'pear', 'orange')