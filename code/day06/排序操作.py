'''
@Date: 2020-03-01 11:49:02
@LastEditors: gxm
@LastEditTime: 2020-03-01 11:52:53
@FilePath: \Python workplace\code\day06\排序操作.py
'''
list1 = ['orange','apple','zoo','internationalization','blueberry']
list2 = sorted(list1)
list3 = sorted(list1,reverse=True)

list4 = sorted(list1,key=len)
print(list1) # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(list2) # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
print(list3) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print(list4) # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

list1.sort(reverse=True)
print(list1) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']