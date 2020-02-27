# 分支结构

## if语句的使用

```python
username = input("输入用户名：")
password = input("输入密码：")
if username == 'admin' and password == 'admin':
  print('身份认证成功')
else: 
  print('身份认证失败')
  # 注意python的格式
```

### 分支嵌套

```python
# if elif else
value = float(input("请输入长度："))
unit = input("请输入单位：")
if unit == 'in' or unit == '英寸':
  print('%f英寸 = %f厘米' % (value,value*2.45))
elif unit =='cm' or unit == '厘米':
  print('%f厘米 = %f 英寸' % (value,value/2.45))
else:
  print('请输入有效单位')
```