'''
@Date: 2020-03-02 19:29:41
@LastEditors: gxm
@LastEditTime: 2020-03-02 19:41:47
@FilePath: \Python workplace\code\day06\集合的基本操作.py
'''
# 创建集合的字面量语法
set1 = {1,2,3,4,5,6,7}
print(set1) # {1, 2, 3, 4, 5, 6, 7}
print(len(set1)) # 7

# 创建集合的构造器语法
set2 = set(range(1,10))
set3 = set((1,3,4,5,0,''))
print(set2,set3) #{1, 2, 3, 4, 5, 6, 7, 8, 9} {0, 1, '', 3, 4, 5}

set4 = {num for num in range(1,100) if num % 5 == 0}
print(set4) #{5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95}
