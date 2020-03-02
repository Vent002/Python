# 字符串和常用数据结构

### 字符串

由零个或多个字符串组成的有限序列

在Python中，把单个或多个字符用单引号或双引号包围起来，表示一个字符串。

1. 转义字符

   使用 ` \` ( 反斜杠)表示转义。 ` \` 后面的字符不再是它原来的意义。

   不希望字符串中的 ` \ ` 表示转义。 可以在字符前面加上字母 `r` 加以说明。

2. 运算符

    ` + ` 实现字符串拼接

    ` * ` 重复一个字符串的内容

   `in` 和 ` not in` 判断一个字符串是否包含另一个字符串

   `[]` 和 ` [ : ]` 运算符从字符串取出某个字符或某些字符

   ```python
   print('hello' * 3) # hello hello hello
   print('hello' * 3 + 'world') # hello hello hello world
   print('ll' in 'hello') # True
   print('world' in 'hello') # False
   str = 'abcde12345'
   # 索引下标从 0 开始
   print(str[2]) # c
   print(str[2:5]) # cde  单冒号表示从索引值到另一索引值
   print(str[2:]) # cde12345 无开始索引或结尾索引 从头开始 到尾结束 
   print(str[2::2]) # ce24 从索引2开始去偶数索引  双冒号
   print(str[::2]) # ace24 偶数索引
   print(str[:-1]) # abcde1234
   print(str[-3:-1]) # 34
   ```

3. 处理字符串的方法

   - ` len() # 计算字符串长度`
   - ` capitalize() # 获取字符串首字母大写的拷贝`
   - ` title() # 获得每个单词首字母大写的拷贝`
   - ` upper() # 获得字符串变大写后的拷贝`
   - ` find() # 从字符串中查找子串所在的位置`
   - ` startswith() # 检查字符串是否以指定字符串开头`
   - ` endswith()  # 检查字符串是否以指定字符串结尾`
   - ` center(number,'字符') # 指定宽度居中在两侧填充指定字符` 
   - ` rjust(number,'字符') # 指定宽度靠右放置左侧填充指定字符` 
   - ` isdigit() # 检查字符串是否由数字构成`
   - ` isalpha() # 检查字符串是否由字母构成`
   - ` isalnum() # 检查字符串是否由数字和字母构成`
   - ` strip() #获得字符串修剪左右两侧空格之后的拷贝`

   字符串格式化

   ```python
   a,b = 5 , 10
   print('{0} * {1} = {2}'.format(a, b, b*a))
   
   c,d = 10, 3
   print(f'{c} * {d} = {c * d}')
   ```

   ### 使用列表

   ​			列表 是一种结构化的、非标量类型，它是值的有序序列，每个值都可以通过索引进行标识，定义列表可以将列表元素放 `[]` 中，多个元素用` ,` 进行分隔，可以使用for循环对列表元素进行遍历，也可以使用`[]` 或`[:]`运算符取出列表中的一个或多个元素

   ```python
   # 列表基本操作
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
   ```
   
   ```python
   # 列表元素的添加和删除
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
   ```
   
   #### 切片操作
   
   ```python
   fruits = ['grape','apple','strawberry','banana']
   fruits += ['pitaya','pear','mango']
   # 列表切片
   fruits2 = fruits[1:4]
   print(fruits2) # ['apple', 'strawberry', 'banana']
   
   fruits3 = fruits2[:]
   print(fruits3) # ['apple', 'strawberry', 'banana']
   
   fruits4 = fruits[-3:-1]
   print(fruits4) # ['pitaya', 'pear']
   fruits5 = fruits[::-1]
   print(fruits5) # ['mango', 'pear', 'pitaya', 'banana', 'strawberry', 'apple', 'grape']
   ```
   
   #### 列表排序
   
   ```python
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
   ```

### 元组

元组与列表类似 是一种容器数据类型，可以用一个变量来存储多个数据，

不同之处在于元组中的元素不能修改。

多个元素组合到一起就是一个元组。

```python
# 定义元组
t = ('hsm',18,True,'beautiful') 
print(t) #('hsm', 18, True, 'beautiful')
# 获取元组中的元素
print(t[0])  #beautiful
print(t[3]) #beautiful
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
```

### 集合

不允许有重复的元素，可以进行交集、并集、差运算

```python
# 创建集合的字面量语法
set1 = {1,2,3,4,5,6,7}
print(set1) # {1, 2, 3, 4, 5, 6, 7}
print(len(set1)) # 7

# 创建集合的构造器语法
set2 = set(range(1,10))
set3 = set((1,3,4,5,0,''))
print(set2,set3) {1, 2, 3, 4, 5, 6, 7, 8, 9} {0, 1, '', 3, 4, 5}

set4 = {num for num in range(1,100) if num % 5 == 0}
print(set4) #{5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95}
```

### 字典

是一种可变容器模型。存储任意类型对象，字典每个元素是有一个键和一个值组成的''键值对'',键和值通过冒号分开。

```python
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
```

