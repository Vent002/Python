# 循环结构

### Python 循环

- ` for - in`
- `  while `

#### for-in

明确知道循环执行的次数或者要对一个容器进行迭代，使用 ` for - in` 

```python
#求1~100的和

'''
@Date: 2020-02-27 10:11:52
@LastEditors: gxm
@LastEditTime: 2020-02-27 10:12:33
@FilePath: \Python workplace\第三天循环结构\100的和.py
'''
sum = 0
for x in range(101):
  sum += x
print(sum)
# range()函数用于构造一个取值范围
# range(101) 产生0~100的整数序列
# range(1,100) 产生1~99的整数序列
# rangge(1,100,2) 产生1~99的奇数序列，其中 2 是步长
```

```python
# for循环实现1~100偶数和
'''
@Date: 2020-02-27 10:17:56
@LastEditors: gxm
@LastEditTime: 2020-02-27 10:20:11
@FilePath: \Python workplace\第三天循环结构\100以内偶数和.py
'''
sum = 0
for x in range(0,101,2):
  sum += x
print(sum)
```

```python
# 九九乘法表 嵌套循环
'''
@Date: 2020-02-27 10:38:27
@LastEditors: gxm
@LastEditTime: 2020-02-27 10:42:28
@FilePath: \Python workplace\第三天循环结构\九九乘法表.py
'''
for i in range(1,10):
  for j in range(1,i+1): #若 i+1换为10输出完整乘法表
    print("%d * %d = %d" % (i,j,i*j) , end='\t') # \t 制表符
  print()
```



#### while 循环

构造不知道具体循环次数的循环结构，使用 ` while ` 循环 ，` while `循环通过一个能够产生或转换出布尔值的表达式控制循环，表达式的值为 ` True ` 循环继续，或者跳出循环

```Python
# while循环+分支结构 猜数游戏
'''
@Date: 2020-02-27 10:22:53
@LastEditors: gxm
@LastEditTime: 2020-02-27 10:28:51
@FilePath: \Python workplace\第三天循环结构\猜数游戏.py
'''
import random
answer = random.randint(1,100)
counter = 0 # 计数
while True:
  counter += 1
  number=int(input('请输入：'))
  if number > answer:
    print('猜大了')
  elif number < answer:
    print('猜小了')
  else:
    print('猜对了')
    break # break 只能跳出当前循环
    			# continue 结束本次循环，
      		# continue后的代码不执行，开始下一次循环
print('总共猜了 %d 次' % counter)
if counter > 7:
  print('游戏结束')
```

