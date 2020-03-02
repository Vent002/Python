'''
@Date: 2020-03-02 19:37:35
@LastEditors: gxm
@LastEditTime: 2020-03-02 19:49:10
@FilePath: \Python workplace\code\day06\集合元素的添加和删除.py
'''
set1 = {1,2,3,4,5,6,7}
set2 = set(range(1,10))
set3 = set((1,3,4,5,0,''))
set1.add(3)
set1.add(1)
set2.update([11,2])
set2.discard(4)
if 9 in set2:
  set2.remove(9)
print(set1,set2) # {1, 2, 3, 4, 5, 6, 7} {1, 2, 3, 5, 6, 7, 8, 11}
print(set3.pop()) # 0
print(set3) # {1, '', 3, 4, 5}
# 集合成员、交集、并集、差集
print(set1 & set2) # {1, 2, 3, 5, 6, 7} set1.intersection(set2)
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 11} set1.union(set2)
print(set1 - set2) # {4} set1.difference(set2)
print(set1 ^ set2) # {4, 8, 11} set1.symmetric_difference(set2)
print(set2 <= set1) # False set2.issubset(set1)
print(set3 <= set1) # False
print(set1.issuperset(set2)) # set1 >= set2 False

